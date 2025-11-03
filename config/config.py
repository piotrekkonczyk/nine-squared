class Config:
    key_above: str
    key_below: str

    def __init__(self, k_above: str | None = None, k_below: str | None = None) -> None:
        self.key_above = k_above if k_above else "k"
        self.key_below = k_below if k_below else "j"
