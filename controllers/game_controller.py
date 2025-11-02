from config.config import Config
from constants.cards_constants import CARD_VALUES_MAP
from constants.deck_constants import CARDS_IN_DECK, CARDS_IN_ROW_ON_SQUARE
from controllers.deck_controller import DeckController

from models.deck import Deck
from utils.cli_colors import error, success


class Game:
    deck: Deck
    config: Config
    deck_controller: DeckController

    def __init__(self, config) -> None:
        self.config = config
        self.deck_core_controller = DeckCoreController()

        self.deck = self.deck_core_controller.create_deck()

    def display_cards(self) -> None:
        text_in_current_row = ""
        cards_left = CARDS_IN_DECK - self.deck.current_card_idx

        print(f"\n{cards_left} left in the deck\n")

        for idx, card_on_square_arr in enumerate(self.deck.cards_on_square):
            if self.is_pile_closed(pile_idx=idx):
                text_in_current_row += "XX" + "     "
            else:
                text_in_current_row += str(card_on_square_arr[0]) + "     "

            # INFO: Print once per three cards or after the last one
            if (
                idx % CARDS_IN_ROW_ON_SQUARE == CARDS_IN_ROW_ON_SQUARE - 1
                or idx + 1 == len(self.deck.cards_on_square)
            ):
                print(f"{text_in_current_row}\n")
                text_in_current_row = ""

    def check_if_value_is_present(self) -> bool:
        top_card_value = CARD_VALUES_MAP[self.deck.card_on_top.value]

        for idx, card_on_square in enumerate(self.deck.cards_on_square):
            if CARD_VALUES_MAP[
                card_on_square[0].value
            ] == top_card_value and not self.is_pile_closed(idx):
                print("NOTE: card is on the table")
                return True

        return False

    def is_game_over(self) -> bool:
        if len(self.deck.cards_on_square) == len(self.deck.closed_piles_indices):
            self.game_lost()
            return True

        if self.deck.current_card_idx == CARDS_IN_DECK:
            self.game_won()
            return True

        return False

    def open_pile(self, pile_idx: int | None = None) -> None:
        if pile_idx:
            self.deck.closed_piles_indices.remove(pile_idx)
            print(f"Pile {pile_idx + 1} opened")
            return

        # NOTE: Not displaying indices
        sorted_indices = [idx + 1 for idx in sorted(self.deck.closed_piles_indices)]

        pile_to_open = int(input(f"Open one of {sorted_indices} piles: "))

        for pile_idx in self.deck.closed_piles_indices:
            if pile_idx + 1 == pile_to_open:
                self.deck.closed_piles_indices.remove(pile_idx)
                return

    def close_pile(self, pile_idx: int):
        self.deck.closed_piles_indices.add(pile_idx)

    def is_pile_closed(self, pile_idx: int) -> bool:
        return pile_idx in self.deck.closed_piles_indices

    def guess(self) -> None:
        guess_input = input("Guess: ")
        guess_elements = guess_input.split(" ")

        # TODO: for now let's assume that the input is always correct

        card_value = CARD_VALUES_MAP[guess_elements[0]]
        key = guess_elements[1]

        top_card_value = CARD_VALUES_MAP[self.deck.card_on_top.value]

        for idx, card_on_square in enumerate(self.deck.cards_on_square):
            if CARD_VALUES_MAP[
                card_on_square[0].value
            ] == card_value and not self.is_pile_closed(idx):
                # NOTE: Unlocked new pile
                if top_card_value == card_value:
                    success("You won! New pile unlocked!")

                    if len(self.deck.closed_piles_indices) == 0:
                        self.deck.cards_on_square.append([self.deck.card_on_top])
                    elif len(self.deck.closed_piles_indices) == 1:
                        self.open_pile(idx)
                    else:
                        self.open_pile()

                # NOTE: Guessed correctly
                elif (
                    top_card_value > card_value
                    and self.config.key_higher == key
                    or top_card_value < card_value
                    and self.config.key_lower == key
                ):
                    self.deck.cards_on_square[idx].insert(0, self.deck.card_on_top)
                    success("You won!")

                # NOTE: Guessed incorrectly
                else:
                    self.deck.cards_on_square[idx].insert(0, self.deck.card_on_top)
                    self.close_pile(idx)
                    error("You lost!")

                print(f"The card was {self.deck.card_on_top}")
                break

        self.deck.current_card_idx += 1

        if self.deck.current_card_idx == CARDS_IN_DECK:
            return

        self.deck.card_on_top = self.deck.cards[self.deck.current_card_idx]

    def game_lost(self):
        error("You have lost. Try once again!")

    def game_won(self):
        success("You won! Huge congrats")
