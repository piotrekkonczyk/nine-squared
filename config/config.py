class Config:
    key_higher: str
    key_lower: str

    def __init__(self, key_higher: str | None, key_lower: str | None) -> None:
        self.key_higher = key_higher if key_higher else "k"
        self.key_lower = key_lower if key_lower else "j"
