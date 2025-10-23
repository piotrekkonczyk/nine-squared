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

    def display_cards(self, cards: list[Card]) -> None:
        displayed_text = ""

        for i in range(9):
            displayed_text += str(cards[i]) + "     "

            if i % 3 == 2:
                print(f"{displayed_text}\n\n")
                displayed_text = ""
