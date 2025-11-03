import pytest
from controllers import game_controller
from controllers.game_controller import Game
from config.config import Config
from models.card import Card


@pytest.fixture
def game():
    g = Game(Config())
    g.deck.cards_on_square = [
        [Card("2", "Clubs")],
        [Card("5", "Diamonds")],
        [Card("9", "Hearts")],
    ]
    g.deck.card_on_top = Card("5", "Spades")
    g.deck.current_card_idx = 3
    return g


def test_guess_incorrect_key(monkeypatch, game):
    monkeypatch.setattr("builtins.input", lambda _: "5 x")
    called = {}
    monkeypatch.setattr(game_controller, "error", lambda m: called.setdefault("msg", m))

    game.guess()
    assert "key is incorrect" in called["msg"].lower()


def test_guess_no_card_on_square(monkeypatch, game):
    monkeypatch.setattr("builtins.input", lambda _: "A k")
    called = {}
    monkeypatch.setattr(game_controller, "error", lambda m: called.setdefault("msg", m))

    game.guess()
    assert "no `a` on the square" in called["msg"].lower()


def test_guess_correct_same_value(monkeypatch, game):
    monkeypatch.setattr("builtins.input", lambda _: "5 k")
    success_calls = []
    monkeypatch.setattr(game_controller, "success", lambda m: success_calls.append(m))

    game.guess()
    assert any("new pile unlocked" in msg.lower() for msg in success_calls)


def test_guess_correct_lower_value(monkeypatch, game):
    monkeypatch.setattr("builtins.input", lambda _: "2 k")
    success_calls = []
    monkeypatch.setattr(game_controller, "success", lambda m: success_calls.append(m))

    game.guess()
    assert any("you won" in msg.lower() for msg in success_calls)
    assert game.deck.current_card_idx == 4


def test_guess_incorrect_direction(monkeypatch, game):
    monkeypatch.setattr("builtins.input", lambda _: "9 k")
    error_calls = []
    monkeypatch.setattr(game_controller, "error", lambda m: error_calls.append(m))

    game.guess()
    assert any("you lost" in msg.lower() for msg in error_calls)
