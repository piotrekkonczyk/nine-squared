from config.config import Config
from constants.cards import CARD_COLORS, CARD_VALUES, CARD_VALUES_MAP
from models.card import Card
from random import shuffle

from models.deck import Deck


class DeckController:
    deck: Deck
    config: Config

    def __init__(self, config) -> None:
        self.config = config

    # NOTE: Behaves kinda like constructor
    def create_deck(self) -> None:
        self.deck = Deck()
        self.seed_deck()

    def seed_deck(self) -> None:
        cards: list[Card] = []
        color_idx = 0

        for i in range(52):
            value_idx = i % 13

            card = Card(value=CARD_VALUES[value_idx], color=CARD_COLORS[color_idx])
            cards.append(card)

            # NOTE: Checks whether the value_index means that the card is ACE, idx 12 means ACE
            if value_idx == 13 - 1:
                color_idx += 1

        shuffle(cards)

        self.deck.cards = cards
        self.deck.cards_on_square = self.deck.cards[0:9]
        self.deck.card_on_top = self.deck.cards[9]

    def display_cards(self) -> None:
        displayed_text = ""

        square_cards_count = len(self.deck.cards_on_square)
        cards_left = 52 - square_cards_count

        print(f"{square_cards_count} cards on the square")
        print(f"{cards_left} left in the deck\n")

        for i in range(9):
            displayed_text += str(self.deck.cards[i]) + "     "

            if i % 3 == 2:
                print(f"{displayed_text}\n")
                displayed_text = ""

    def check_if_value_is_present(self):
        top_card_value = CARD_VALUES_MAP[self.deck.card_on_top.value]

        for card_on_square in self.deck.cards_on_square:
            if CARD_VALUES_MAP[card_on_square.value] == top_card_value:
                print("NOTE: card is on the table")
                return True

        return False

    def guess(self) -> None:
        guess_input = input("Guess: ")
        guess_elements = guess_input.split(" ")

        # TODO: for now let's assume that the input is always correct

        card_value = CARD_VALUES_MAP[guess_elements[0]]
        key = guess_elements[1]

        top_card_value = CARD_VALUES_MAP[self.deck.card_on_top.value]

        for card_on_square in self.deck.cards_on_square:
            if CARD_VALUES_MAP[card_on_square.value] == card_value:
                if top_card_value == card_value:
                    print("You won! New pile unlocked!")
                if top_card_value > card_value and self.config.key_higher == key:
                    print("You won!")
                elif top_card_value < card_value and self.config.key_lower == key:
                    print("You won!")
                else:
                    print("You lost!")

                print(f"The card was {self.deck.card_on_top}")

                break
