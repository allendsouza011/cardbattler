from .deck import Deck

class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.deck = Deck()
        self.hand = []

    def draw_initial_hand(self):
        self.hand = [self.deck.draw_card() for _ in range(5)]

    def play_card(self, index):
        if index < len(self.hand):
            return self.hand.pop(index)
        return None
