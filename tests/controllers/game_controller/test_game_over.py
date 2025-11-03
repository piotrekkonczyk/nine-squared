import pytest
from controllers.game_controller import Game
from config.config import Config


@pytest.fixture
def game():
    return Game(Config())


def test_game_over_when_all_piles_closed(capsys, game):
    game.deck.closed_piles_indices = set(range(len(game.deck.cards_on_square)))

    assert game.is_over()

    captured = capsys.readouterr()
    assert "lost" in captured.out.lower()


def test_game_over_when_deck_finished(capsys, game):
    game.deck.current_card_idx = 52

    assert game.is_over()

    captured = capsys.readouterr()
    assert "congrats" in captured.out.lower()


def test_game_not_over(game):
    assert not game.is_over()
