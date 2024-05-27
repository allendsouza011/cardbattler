class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.deck = None
        self.hand = []
        self.mana = 5
        self.max_mana = 5

    def draw_card(self):
        card = self.deck.draw_card()
        if card:
            self.hand.append(card)

    def draw_initial_hand(self, count=5):
        for _ in range(count):
            self.draw_card()

    def play_card(self, card_index):
        if 0 <= card_index < len(self.hand):
            return self.hand.pop(card_index)
        return None

    def regenerate_mana(self):
        self.mana = min(self.mana + 1, self.max_mana)
