from controllers.deck_controller import DeckController
from constants.deck_constants import (
    CARDS_IN_DECK,
    CARDS_ON_SQUARE_BY_DEFAULT,
)
from models.deck import Deck
from models.card import Card


def test_create_deck_returns_deck_instance():
    controller = DeckController()
    deck = controller.create_deck()

    assert isinstance(deck, Deck)
    assert isinstance(deck.cards, list)
    assert isinstance(deck.cards_on_square, list)
    assert isinstance(deck.closed_piles_indices, set)
    assert len(deck.cards) == CARDS_IN_DECK
    assert deck.current_card_idx == CARDS_ON_SQUARE_BY_DEFAULT
    assert isinstance(deck.card_on_top, Card)
    assert all(isinstance(pile, list) for pile in deck.cards_on_square)
