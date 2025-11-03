from config.config import Config
from controllers.game_controller import Game

config = Config()

game = Game(config=config)

print(
    "Separate card value and higher/lower decision with space. So your guess might look like `Q k`"
)

while not game.is_over():
    print(game.deck.card_on_top)
    game.display_cards()

    game.check_if_value_is_present()
    game.guess()
