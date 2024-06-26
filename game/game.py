import pygame
import random
from .player import Player
from .deck import Deck

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Player("Player", 20)
        self.ai = Player("AI", 20)
        self.difficulty = 1
        self.selected_card = None
        self.turn = "player"
        self.round = 1
        self.buff = None
        self.buff_rounds_left = 0
        self.score = 0
        self.draft_cards()
        self.load_assets()
    
    def load_assets(self):
        self.card_back = pygame.image.load('assets/card_back.png')

    def draft_cards(self):
        self.player.deck = Deck()
        self.ai.deck = Deck(difficulty=self.difficulty)
        self.player.hand = []
        self.ai.hand = []
        draft_pool = [self.player.deck.draw_card() for _ in range(10)]
        self.draft_selection(draft_pool)

    def draft_selection(self, draft_pool):
        selecting = True
        selected_cards = 0
        while selecting:
            self.screen.fill((255, 255, 255))
            font = pygame.font.Font(None, 36)
            draft_text = font.render("Select 5 Cards:", True, (0, 0, 0))
            self.screen.blit(draft_text, (300, 10))

            for i, card in enumerate(draft_pool):
                if card:  # Ensure the card is not None
                    text = font.render(str(card), True, (0, 0, 0))
                    card_rect = pygame.Rect(50, 50 + i * 40, 700, 30)
                    pygame.draw.rect(self.screen, (200, 200, 200), card_rect)
                    self.screen.blit(text, (50, 50 + i * 40))

            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    selecting = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for i, card in enumerate(draft_pool):
                        card_rect = pygame.Rect(50, 50 + i * 40, 700, 30)
                        if card_rect.collidepoint(event.pos) and card:
                            self.player.hand.append(card)
                            draft_pool[i] = None
                            selected_cards += 1
                            if selected_cards == 5:
                                selecting = False
                            break

    def run(self):
        pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
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
            card_rect = pygame.Rect(50 + i * 100, self.screen.get_height() - 100, 80, 120)
            if card_rect.collidepoint(event.pos):
                self.selected_card = i
                self.player_turn()

    def player_turn(self):
        if self.selected_card is not None:
            card = self.player.play_card(self.selected_card)
            if card:
                self.resolve_combat(card, self.ai)
                self.turn = "ai"
            self.selected_card = None

    def ai_turn(self):
        if self.ai.hand:
            card = self.ai.play_card(0)
            if card:
                self.resolve_combat(card, self.player)
                self.turn = "player"

    def resolve_combat(self, card, opponent):
        opponent.health -= card.attack
        card.apply_ability(opponent, self.player if self.turn == "player" else self.ai)
        if opponent.health < 0:
            opponent.health = 0

def draw_ui(self):
    font = pygame.font.Font(None, 36)
    
    # Draw health bars
    player_health_text = font.render(f"Player Health: {self.player.health}", True, (0, 0, 0))
    ai_health_text = font.render(f"AI Health: {self.ai.health}", True, (0, 0, 0))
    score_text = font.render(f"Score: {self.score}", True, (0, 0, 0))
    self.screen.blit(player_health_text, (50, self.screen.get_height() // 2 - 50))
    self.screen.blit(ai_health_text, (650, self.screen.get_height() // 2 - 50))
    self.screen.blit(score_text, (350, self.screen.get_height() // 2 - 50))

    # Draw player's cards at the bottom
    for i, card in enumerate(self.player.hand):
        text = font.render(f"{card.name} (ATK: {card.attack}, DEF: {card.defense}, ABILITY: {card.ability})", True, (0, 0, 0))
        card_rect = pygame.Rect(50 + i * 100, self.screen.get_height() - 150, 200, 30)
        pygame.draw.rect(self.screen, (200, 200, 200), card_rect)
        self.screen.blit(text, (50 + i * 100, self.screen.get_height() - 150))

    # Draw AI's card backs at the top
    for i in range(len(self.ai.hand)):
        card_rect = pygame.Rect(50 + i * 100, 50, 80, 120)
        self.screen.blit(self.card_back, card_rect)


    def check_game_over(self):
        if self.player.health == 0:
            print("AI wins!")
            self.running = False
        elif self.ai.health == 0:
            print("Player wins!")
            self.score += 1
            self.round += 1
            if self.round % 2 == 0:
                self.apply_buff()
            self.player.health = 20
            self.difficulty += 1
            self.ai = Player("AI", 20 + self.difficulty * 5)
            self.ai.deck = Deck(difficulty=self.difficulty)
            self.ai.draw_initial_hand()
            self.player.deck = Deck()
            self.draft_cards()
            self.turn = "player"

    def apply_buff(self):
        buffs = ["common", "rare", "epic"]
        buff = random.choice(buffs)
        if buff == "common":
            self.buff_rounds_left = 1
            self.player.health += 5
        elif buff == "rare":
            self.buff_rounds_left = 2
            self.player.health += 10
        elif buff == "epic":
            self.buff_rounds_left = 3
            self.player.health += 15
        print(f"Player received a {buff} buff for {self.buff_rounds_left} rounds.")
