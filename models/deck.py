from controllers.deck_controller import DeckController
from models.card import Card


class Deck:
    cards: list[Card]
    deck_controller: DeckController

    def seed_cards(self) -> None:
        self.cards = self.deck_controller.seed_cards()

    def shuffle_cards(self) -> None:
        pass

    def __init__(self) -> None:
        self.deck_controller = DeckController()
        self.seed_cards()
