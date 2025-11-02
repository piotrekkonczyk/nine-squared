from random import shuffle
from constants.cards_constants import CARD_COLORS, CARD_VALUES
from constants.deck_constants import (
    CARDS_IN_COLOR,
    CARDS_IN_DECK,
    CARDS_ON_SQUARE_BY_DEFAULT,
)
from models.card import Card
from models.deck import Deck


class DeckController:
    # NOTE: Behaves kinda like constructor
    def create_deck(self) -> Deck:
        deck = Deck()
        deck.closed_piles_indices = set()
        deck.cards_on_square = []

        self.seed_deck(deck=deck)

        return deck

    def seed_deck(self, deck: Deck) -> None:
        deck.cards = []
        color_idx = 0

        for i in range(CARDS_IN_DECK):
            value_idx = i % CARDS_IN_COLOR

            card = Card(value=CARD_VALUES[value_idx], color=CARD_COLORS[color_idx])
            deck.cards.append(card)

            # NOTE: Checks whether the value_index means that the card is ACE, idx 12 means ACE
            if value_idx == CARDS_IN_COLOR - 1:
                color_idx += 1

        shuffle(deck.cards)

        # NOTE: Seeding cards on square as a two-dimensional array
        for i in range(CARDS_ON_SQUARE_BY_DEFAULT):
            deck.cards_on_square.append([deck.cards[i]])

        deck.card_on_top = deck.cards[CARDS_ON_SQUARE_BY_DEFAULT]
        deck.current_card_idx = CARDS_ON_SQUARE_BY_DEFAULT
