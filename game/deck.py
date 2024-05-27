import random
from .card import Card

class Deck:
    def __init__(self, difficulty=1):
        self.cards = self.generate_cards(difficulty)

    def generate_cards(self, difficulty):
        cards = []
        abilities = [None, "heal", "damage", "boost"]
        for i in range(20):
            attack = random.randint(1, 10) + difficulty
            ability = random.choice(abilities)
            cards.append(Card(f"Card {i+1}", attack, ability))
        return cards

    def draw_card(self):
        return self.cards.pop(random.randint(0, len(self.cards) - 1))
