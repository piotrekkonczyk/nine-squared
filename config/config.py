class Config:
    key_higher: str
    key_lower: str

    def __init__(self, k_higher: str | None = None, k_lower: str | None = None) -> None:
        self.key_higher = k_higher if k_higher else "k"
        self.key_lower = k_lower if k_lower else "j"
