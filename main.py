from config.config import Config
from controllers.deck_controller import DeckController

config = Config()

deck_controller = DeckController(config=config)
deck_controller.create_deck()

deck_controller.display_cards()

deck_controller.guess()
