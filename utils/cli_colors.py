from colorama import Fore, Style, init
from models.card import Card


def init_cli_colors():
    init()


def success(message: str):
    print(Fore.LIGHTGREEN_EX + message + Style.RESET_ALL)


def error(message: str):
    print(Fore.LIGHTRED_EX + message + Style.RESET_ALL)


def print_colorized_card(card: Card):
    color = ""
    if card.color == "Spades" or card.color == "Clubs":
        color = Fore.BLACK
    else:
        color = Fore.RED

    print(color + str(card))
