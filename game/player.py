from game.card import Card
import random

class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.deck = []
        self.hand = []

    def draw_card(self):
        if self.deck:
            self.hand.append(self.deck.pop())

    def draw_initial_hand(self, count=5):
        for _ in range(count):
            self.draw_card()

    def play_card(self, card_index):
        if 0 <= card_index < len(self.hand):
            return self.hand.pop(card_index)
        return None
