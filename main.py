import pygame
from game.game import Game
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Endless Card Battler")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game variables
clock = pygame.time.Clock()
running = True

class Card:
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense

    def __str__(self):
        return f"{self.name} (ATK: {self.attack}, DEF: {self.defense})"

class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.deck = self.build_deck()
        self.hand = []

    def build_deck(self):
        # Create a simple deck with random cards
        return [Card(f"Card {i}", random.randint(1, 10), random.randint(1, 10)) for i in range(30)]

    def draw_card(self):
        if self.deck:
            self.hand.append(self.deck.pop())

    def play_card(self, card_index):
        if 0 <= card_index < len(self.hand):
            return self.hand.pop(card_index)
        return None

# Create players
player = Player("Player", 20)
ai = Player("AI", 20)

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill(WHITE)

    # Draw player and AI hands
    font = pygame.font.Font(None, 36)
    for i, card in enumerate(player.hand):
        text = font.render(str(card), True, BLACK)
        screen.blit(text, (50, 50 + i * 30))

    for i, card in enumerate(ai.hand):
        text = font.render(str(card), True, BLACK)
        screen.blit(text, (450, 50 + i * 30))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Endless Card Battler")
    game = Game(screen)
    game.run()

if __name__ == "__main__":
    main()
