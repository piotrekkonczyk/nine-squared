from models.card import Card


class Deck:
    cards: list[Card]

    def seed_cards(self):
        for i in range(52):
            print(f"Seeding cards, {52 - i} left...")

    def __init__(self) -> None:
        self.seed_cards()
