import pygame
from game.player import Player
from game.deck import Deck

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Player("Player", 20)
        self.ai = Player("AI", 20)
        self.player.deck = Deck()
        self.ai.deck = Deck()
        self.player.draw_initial_hand()
        self.ai.draw_initial_hand()
        self.turn = "player"  # "player" or "ai"
        self.difficulty = 1  # Starting difficulty
        self.selected_card = None  # To track selected card

    def run(self):
        while self.running:
            self.handle_events()
            self.screen.fill((255, 255, 255))
            self.draw_ui()
            pygame.display.flip()
            self.clock.tick(30)

            if self.turn == "ai":
                self.ai_turn()

            self.check_game_over()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and self.turn == "player":
                self.handle_mouse_event(event)

    def handle_mouse_event(self, event):
        for i, card in enumerate(self.player.hand):
            card_rect = pygame.Rect(50, 400 + i * 40, 200, 30)
            if card_rect.collidepoint(event.pos):
                self.selected_card = i
                self.player_turn()

    def player_turn(self):
        if self.selected_card is not None:
            card = self.player.play_card(self.selected_card)
            self.resolve_combat(card, self.ai)
            self.turn = "ai"
            self.selected_card = None

    def ai_turn(self):
        if self.ai.hand:
            card = self.ai.play_card(0)
            self.resolve_combat(card, self.player)
            self.turn = "player"

    def resolve_combat(self, card, opponent):
        opponent.health -= card.attack
        if opponent.health < 0:
            opponent.health = 0

    def draw_ui(self):
        font = pygame.font.Font(None, 36)

        for i, card in enumerate(self.player.hand):
            text = font.render(str(card), True, (0, 0, 0))
            card_rect = pygame.Rect(50, 400 + i * 40, 200, 30)
            pygame.draw.rect(self.screen, (200, 200, 200), card_rect)
            self.screen.blit(text, (50, 400 + i * 40))

        for i, card in enumerate(self.ai.hand):
            text = font.render(str(card), True, (0, 0, 0))
            self.screen.blit(text, (450, 50 + i * 40))

        player_health_text = font.render(f"Player Health: {self.player.health}", True, (0, 0, 0))
        ai_health_text = font.render(f"AI Health: {self.ai.health}", True, (0, 0, 0))
        self.screen.blit(player_health_text, (50, 10))
        self.screen.blit(ai_health_text, (450, 10))

    def check_game_over(self):
        if self.player.health == 0:
            print("AI wins!")
            self.running = False
        elif self.ai.health == 0:
            print("Player wins!")
            self.difficulty += 1
            self.ai = Player("AI", 20 + self.difficulty * 5)
            self.ai.deck = Deck(difficulty=self.difficulty)
            self.ai.draw_initial_hand()
            self.player.health = min(self.player.health + 5, 20)
            self.player.deck = Deck()
            self.player.draw_initial_hand()
            self.turn = "player"
