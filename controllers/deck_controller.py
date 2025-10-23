from constants.cards import CARD_COLORS, CARD_VALUES
from models.card import Card
from random import shuffle


class DeckController:
    def seed_cards(self) -> list[Card]:
        cards: list[Card] = []
        color_idx = 0

        for i in range(52):
            value_idx = i % 13

            card = Card(value=CARD_VALUES[value_idx], color=CARD_COLORS[color_idx])
            cards.append(card)

            if i % 13 == 13 - 1:
                color_idx += 1

        return cards

    def shuffle_cards(self, cards: list[Card]) -> list[Card]:
        shuffle(cards)

        return cards

    def display_cards(self, cards: list[Card], cards_on_square: list[Card]) -> None:
        displayed_text = ""
        square_cards_count = len(cards_on_square)

        print(f"{square_cards_count} cards on the square")
        print(f"{52 - square_cards_count} left in the deck")
        print("")

        for i in range(9):
            displayed_text += str(cards[i]) + "     "

            if i % 3 == 2:
                print(f"{displayed_text}")

                if i == 8:
                    return

                print("\n")

                displayed_text = ""
