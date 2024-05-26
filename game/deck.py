from game.card import Card
import random

class Deck:
    def __init__(self, difficulty=1):
        self.cards = [Card(f"Card {i}", random.randint(1, 10) * difficulty, random.randint(1, 10) * difficulty) for i in range(30)]
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop() if self.cards else None
