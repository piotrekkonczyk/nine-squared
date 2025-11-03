from config.config import Config


def test_defaults_are_set_correctly():
    cfg = Config()
    assert cfg.key_above == "k"
    assert cfg.key_below == "j"


def test_custom_keys_are_applied():
    cfg = Config(k_above="w", k_below="s")
    assert cfg.key_above == "w"
    assert cfg.key_below == "s"


def test_partial_customization():
    cfg1 = Config(k_above="i")
    cfg2 = Config(k_below="n")

    assert cfg1.key_above == "i"
    assert cfg1.key_below == "j"  # default

    assert cfg2.key_above == "k"  # default
    assert cfg2.key_below == "n"
