from config.config import Config
from controllers.game_controller import Game
import typer

from utils.print_game_rules import print_game_rules

app = typer.Typer(name="Nine Squared")


@app.command()
def main(
    rules: bool = typer.Option(False, "--rules", help="Show game rules and exit."),
):
    if rules:
        print_game_rules()
        raise typer.Exit()

    config = Config()
    game = Game(config=config)

    typer.echo(
        "Separate card value and higher/lower decision with space. "
        "So your guess might look like `Q k`"
    )

    while not game.is_over():
        game.display_cards()
        game.check_if_value_is_present()

        game.guess()


if __name__ == "__main__":
    app()
