import pygame
from game import Game

def main():
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Card Battler")
    game = Game(screen)
    game.run()
    pygame.quit()

if __name__ == "__main__":
    main()
