from constants.cards import CARD_COLORS, CARD_VALUES
from models.card import Card
from random import shuffle

from models.deck import Deck


class DeckController:
    deck: Deck

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
