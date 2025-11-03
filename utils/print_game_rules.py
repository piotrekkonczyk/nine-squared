from rich.console import Console
from rich.markdown import Markdown


def print_game_rules():
    with open("GAME_RULES.md") as file:
        console = Console()
        markdown_rules = Markdown(file.read())

        console.print(markdown_rules)
