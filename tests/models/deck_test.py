import pytest
from models.card import Card
from models.deck import Deck


@pytest.fixture
def sample_cards():
    return [
        Card("A", "Hearts"),
        Card("K", "Spades"),
        Card("Q", "Diamonds"),
    ]


@pytest.fixture
def sample_deck(sample_cards):
    deck = Deck()
    deck.cards = sample_cards
    deck.cards_on_square = [[sample_cards[0]], [sample_cards[1]], [sample_cards[2]]]
    deck.card_on_top = sample_cards[0]
    deck.closed_piles_indices = {1}
    deck.current_card_idx = 0
    return deck


def test_deck_has_cards(sample_deck):
    assert isinstance(sample_deck.cards, list)
    assert all(isinstance(card, Card) for card in sample_deck.cards)
    assert len(sample_deck.cards) == 3


def test_cards_on_square_structure(sample_deck):
    assert isinstance(sample_deck.cards_on_square, list)
    assert all(isinstance(pile, list) for pile in sample_deck.cards_on_square)
    assert all(
        isinstance(card, Card) for pile in sample_deck.cards_on_square for card in pile
    )


def test_card_on_top_is_card(sample_deck):
    assert isinstance(sample_deck.card_on_top, Card)


def test_closed_piles_indices_is_set(sample_deck):
    assert isinstance(sample_deck.closed_piles_indices, set)
    assert 1 in sample_deck.closed_piles_indices


def test_current_card_index(sample_deck):
    assert isinstance(sample_deck.current_card_idx, int)
    assert sample_deck.current_card_idx == 0
