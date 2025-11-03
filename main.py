from config.config import Config
from controllers.game_controller import Game

config = Config()

game = Game(config=config)

while not game.is_over():
    game.display_cards()

    game.check_if_value_is_present()
    game.guess()
