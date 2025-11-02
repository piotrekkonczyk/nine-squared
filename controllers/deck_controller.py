from config.config import Config
from constants.cards_constants import CARD_COLORS, CARD_VALUES, CARD_VALUES_MAP
from constants.deck_constants import (
    CARDS_IN_COLOR,
    CARDS_IN_DECK,
    CARDS_IN_ROW_ON_SQUARE,
    CARDS_ON_SQUARE_BY_DEFAULT,
)
from models.card import Card
from random import shuffle

from models.deck import Deck
from utils.cli_colors import error, success


class DeckController:
    deck: Deck
    config: Config

    def __init__(self, config) -> None:
        self.config = config

    # NOTE: Behaves kinda like constructor
    def create_deck(self) -> None:
        self.deck = Deck()
        self.seed_deck()
        self.deck.closed_piles_indices = set()

    def seed_deck(self) -> None:
        cards: list[Card] = []
        color_idx = 0

        for i in range(CARDS_IN_DECK):
            value_idx = i % CARDS_IN_COLOR

            card = Card(value=CARD_VALUES[value_idx], color=CARD_COLORS[color_idx])
            cards.append(card)

            # NOTE: Checks whether the value_index means that the card is ACE, idx 12 means ACE
            if value_idx == CARDS_IN_COLOR - 1:
                color_idx += 1

        shuffle(cards)

        self.deck.cards = cards

        # NOTE: Seeding cards on square as a two-dimensional array
        self.deck.cards_on_square = []
        for i in range(CARDS_ON_SQUARE_BY_DEFAULT):
            self.deck.cards_on_square.append([self.deck.cards[i]])

        self.deck.card_on_top = self.deck.cards[CARDS_ON_SQUARE_BY_DEFAULT]
        self.deck.current_card_idx = CARDS_ON_SQUARE_BY_DEFAULT

    def display_cards(self) -> None:
        displayed_text = ""

        cards_left = CARDS_IN_DECK - self.deck.current_card_idx

        print(f"\n{cards_left} left in the deck\n")

        for idx, card_on_square_arr in enumerate(self.deck.cards_on_square):
            if self.is_pile_closed(idx):
                displayed_text += "XX" + "     "
            else:
                displayed_text += str(card_on_square_arr[0]) + "     "

            # INFO: Print once per three cards or after the last one
            if (
                idx % CARDS_IN_ROW_ON_SQUARE == CARDS_IN_ROW_ON_SQUARE - 1
                or idx + 1 == len(self.deck.cards_on_square)
            ):
                print(f"{displayed_text}\n")
                displayed_text = ""

    def check_if_value_is_present(self):
        top_card_value = CARD_VALUES_MAP[self.deck.card_on_top.value]

        for idx, card_on_square in enumerate(self.deck.cards_on_square):
            if CARD_VALUES_MAP[
                card_on_square[0].value
            ] == top_card_value and not self.is_pile_closed(idx):
                print("NOTE: card is on the table")
                return True

        return False

    def can_play(self):
        print(self.deck.current_card_idx)

        if len(self.deck.cards_on_square) == len(self.deck.closed_piles_indices):
            self.game_lost()
            return False

        if self.deck.current_card_idx == CARDS_IN_DECK:
            self.game_won()
            return False

        return True

    def open_pile(self):
        # NOTE: Not displaying indices
        sorted_indices = [idx + 1 for idx in sorted(self.deck.closed_piles_indices)]

        pile_to_open = int(input(f"Open one of {sorted_indices} piles: "))

        for pile_idx in self.deck.closed_piles_indices:
            if pile_idx == pile_to_open:
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
                if top_card_value == card_value:
                    success("You won! New pile unlocked!")

                    if len(self.deck.closed_piles_indices) == 0:
                        self.deck.cards_on_square.append([self.deck.card_on_top])
                    else:
                        self.open_pile()

                elif top_card_value > card_value and self.config.key_higher == key:
                    self.deck.cards_on_square[idx].insert(0, self.deck.card_on_top)
                    success("You won!")

                elif top_card_value < card_value and self.config.key_lower == key:
                    self.deck.cards_on_square[idx].insert(0, self.deck.card_on_top)
                    success("You won!")

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
