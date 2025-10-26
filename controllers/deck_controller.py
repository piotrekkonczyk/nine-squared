from constants.cards import CARD_COLORS, CARD_VALUES
from models.card import Card
from random import shuffle

from models.deck import Deck


class DeckController:
    deck: Deck

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

            if i % 13 == 13 - 1:
                color_idx += 1

        shuffle(cards)

        self.deck.cards = cards
        self.deck.cards_on_square = self.deck.cards[0:9]
        self.deck.card_on_top = self.deck.cards[9]

    def display_cards(self) -> None:
        displayed_text = ""
        square_cards_count = len(self.deck.cards_on_square)

        print(f"{square_cards_count} cards on the square")
        print(f"{52 - square_cards_count} left in the deck")
        print("")

        for i in range(9):
            displayed_text += str(self.deck.cards[i]) + "     "

            if i % 3 == 2:
                print(f"{displayed_text}")

                if i == 8:
                    return

                print("\n")

                displayed_text = ""
