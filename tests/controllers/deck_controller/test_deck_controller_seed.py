import pytest
from controllers.deck_controller import DeckController
from constants.cards_constants import CARD_VALUES, CARD_COLORS
from constants.deck_constants import (
    CARDS_IN_COLOR,
    CARDS_IN_DECK,
    CARDS_ON_SQUARE_BY_DEFAULT,
)
from models.deck import Deck
from models.card import Card


@pytest.fixture
def empty_deck():
    deck = Deck()
    deck.closed_piles_indices = set()
    deck.cards_on_square = []
    return deck


def test_seed_deck_creates_correct_number_of_cards(empty_deck):
    controller = DeckController()
    controller.seed_deck(empty_deck)

    assert len(empty_deck.cards) == CARDS_IN_DECK


def test_seed_deck_cards_have_valid_values_and_colors(empty_deck):
    controller = DeckController()
    controller.seed_deck(empty_deck)

    values = {card.value for card in empty_deck.cards}
    colors = {card.color for card in empty_deck.cards}

    assert set(CARD_VALUES).issuperset(values)
    assert set(CARD_COLORS).issuperset(colors)
    assert len(colors) == len(CARD_COLORS)


def test_each_color_has_correct_number_of_cards(empty_deck):
    controller = DeckController()
    controller.seed_deck(empty_deck)

    color_counts = {color: 0 for color in CARD_COLORS}
    for card in empty_deck.cards:
        color_counts[card.color] += 1

    for _, count in color_counts.items():
        assert count == CARDS_IN_COLOR


def test_cards_on_square_seeded_correctly(empty_deck):
    controller = DeckController()
    controller.seed_deck(empty_deck)

    assert len(empty_deck.cards_on_square) == CARDS_ON_SQUARE_BY_DEFAULT
    assert all(isinstance(pile, list) for pile in empty_deck.cards_on_square)
    assert all(
        isinstance(card, Card) for pile in empty_deck.cards_on_square for card in pile
    )
    assert empty_deck.current_card_idx == CARDS_ON_SQUARE_BY_DEFAULT
    assert isinstance(empty_deck.card_on_top, Card)
