from controllers.deck_controller import DeckController
from models.card import Card


class Deck:
    cards: list[Card]
    deck_controller: DeckController

    def seed_cards(self) -> None:
        self.cards = self.deck_controller.seed_cards()

    def shuffle_cards(self) -> None:
        self.cards = self.deck_controller.shuffle_cards(self.cards)

    def __init__(self) -> None:
        self.deck_controller = DeckController()

        self.seed_cards()
        self.shuffle_cards()

    def display_cards(self):
        self.deck_controller.display_cards(self.cards)
