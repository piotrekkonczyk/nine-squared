from models.card import Card


class Deck:
    cards: list[Card]
    cards_on_square: list[Card]
    card_on_top: Card
