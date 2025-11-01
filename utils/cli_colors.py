from colorama import Fore, Style, init


def init_cli_colors():
    init()


def success(message: str):
    print(Fore.LIGHTGREEN_EX + message + Style.RESET_ALL)


def error(message: str):
    print(Fore.LIGHTRED_EX + message + Style.RESET_ALL)


def red_color(value: str):
    return Fore.RED + value + Style.RESET_ALL
