import builtins
import pytest
from controllers.game_controller import Game
from config.config import Config


@pytest.fixture
def game():
    return Game(Config())


def test_close_and_check_pile(game):
    game.close_pile(3)
    assert game.is_pile_closed(3)
    assert 3 in game.deck.closed_piles_indices


def test_open_pile_success(monkeypatch, game: Game):
    # Two closed piles => function should ask for input and succeed when correct index given
    game.deck.closed_piles_indices = {0, 1}
    monkeypatch.setattr(builtins, "input", lambda _: "1")  # open pile 1 (index 0)
    assert game.open_pile()
    assert 0 not in game.deck.closed_piles_indices


def test_open_pile_invalid_input_when_multiple_closed(monkeypatch, game):
    # Multiple closed piles and invalid input => should return False and not remove any index
    game.deck.closed_piles_indices = {0, 1, 2}
    monkeypatch.setattr(builtins, "input", lambda _: "99")  # invalid selection
    assert not game.open_pile()
    # ensure set unchanged
    assert game.deck.closed_piles_indices == {0, 1, 2}


def test_open_pile_auto_opens_when_single(monkeypatch, game):
    # Single closed pile => auto-opens without asking input (by design) and returns True
    game.deck.closed_piles_indices = {0}
    # Even if input is patched to garbage, it shouldn't be called in this branch;
    # function should auto-clear and return True
    monkeypatch.setattr(builtins, "input", lambda _: "99")
    assert game.open_pile()
    assert game.deck.closed_piles_indices == set()
