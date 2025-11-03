from models.card import Card
from utils.cli_colors import red_color


def test_init():
    card = Card(value="A", color="Hearts")

    assert card is not None
    assert card.value == "A"
    assert card.color == "Hearts"


def test_right_colors():
    card_heart = Card(value="A", color="Hearts")
    card_diamond = Card(value="K", color="Diamonds")

    card_spade = Card(value="Q", color="Spades")
    card_club = Card(value="J", color="Clubs")

    assert str(card_heart) == "A " + red_color("\U00002764")
    assert str(card_diamond) == "K " + red_color("\U000025c6")
    assert str(card_spade) == "Q " + "\U00002660"
    assert str(card_club) == "J " + "\U00002663"
