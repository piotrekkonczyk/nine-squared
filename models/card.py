from utils.card_helpers import CardColor, CardValue


class Card:
    value: CardValue
    color: CardColor

    def __init__(self, value: CardValue, color: CardColor) -> None:
        self.value = value
        self.color = color

    def __repr__(self) -> str:
        color = ""

        match self.color:
            case "Hearts":
                color = "\U00002764"
            case "Diamonds":
                color = "\U000025c6"
            case "Spades":
                color = "\U00002660"
            case "Clubs":
                color = "\U00002663"

        return f"{self.value} {color}"
