from card_helpers import CardColor, CardValue


class Card:
    value: CardValue
    color: CardColor

    def __init__(self, value: CardValue, color: CardColor) -> None:
        self.value = value
        self.color = color
