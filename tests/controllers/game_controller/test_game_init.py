from controllers.game_controller import Game
from config.config import Config
from models.deck import Deck
from controllers.deck_controller import DeckController


def test_game_initializes_correctly():
    config = Config()
    game = Game(config)

    assert isinstance(game.config, Config)
    assert isinstance(game.deck_controller, DeckController)
    assert isinstance(game.deck, Deck)
    assert hasattr(game.deck, "cards")
    assert len(game.deck.cards) == 52
    assert game.deck.current_card_idx == 9
