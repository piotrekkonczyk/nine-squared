from constants.cards import CARD_COLORS, CARD_VALUES
from models.card import Card


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
