import pytest
from controllers import game_controller
from controllers.game_controller import Game
from config.config import Config
from utils.error_codes import INVALID_CARD_CHOICE


@pytest.fixture
def game():
    return Game(Config())


def test_invalid_card_choice(monkeypatch, game):
    errors = []
    # patch where the function is used (in controllers.game_controller), not in utils.cli_colors
    monkeypatch.setattr(game_controller, "error", lambda m: errors.append(m))

    result = game.is_guess_valid(INVALID_CARD_CHOICE, game.config.key_above)

    assert result is False
    assert any("invalid card choice" in msg.lower() for msg in errors)


def test_invalid_key(monkeypatch, game):
    errors = []
    monkeypatch.setattr(game_controller, "error", lambda m: errors.append(m))

    result = game.is_guess_valid(5, "x")

    assert result is False
    assert any("key is incorrect" in msg.lower() for msg in errors)


def test_valid_guess(game):
    assert game.is_guess_valid(5, game.config.key_above)
