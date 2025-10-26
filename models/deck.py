from models.card import Card


class Deck:
    cards: list[Card]
    cards_on_square: list[list[Card]]
    card_on_top: Card

    current_card_idx: int
