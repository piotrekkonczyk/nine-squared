import builtins
from colorama import Fore, Style
from utils import cli_colors


def test_init_cli_colors(monkeypatch):
    """Check that init() from colorama is called once."""
    called = {}

    def fake_init():
        called["init_called"] = True

    monkeypatch.setattr("utils.cli_colors.init", fake_init)
    cli_colors.init_cli_colors()
    assert "init_called" in called


def test_red_color_returns_wrapped_text():
    result = cli_colors.red_color("♥")
    assert result == Fore.RED + "♥" + Style.RESET_ALL


def test_success_prints_colored_message(monkeypatch):
    printed = {}

    def fake_print(msg):
        printed["msg"] = msg

    monkeypatch.setattr(builtins, "print", fake_print)
    cli_colors.success("ok!")

    expected = Fore.LIGHTGREEN_EX + "ok!" + Style.RESET_ALL
    assert printed["msg"] == expected


def test_error_prints_colored_message(monkeypatch):
    printed = {}

    def fake_print(msg):
        printed["msg"] = msg

    monkeypatch.setattr(builtins, "print", fake_print)
    cli_colors.error("fail!")

    expected = Fore.LIGHTRED_EX + "fail!" + Style.RESET_ALL
    assert printed["msg"] == expected
