from config.config import Config
from controllers.game_controller import Game


def main():
    config = Config()

    game = Game(config=config)

    print(
        "Separate card value and higher/lower decision with space. So your guess might look like `Q k`"
    )

    while not game.is_over():
        game.display_cards()

        game.check_if_value_is_present()
        game.guess()


if __name__ == "__main__":
    main()
