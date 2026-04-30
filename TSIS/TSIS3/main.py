import pygame
from ui import MainMenu
from racer import Game

pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

menu = MainMenu(screen)

while True:
    action = menu.run()

    if action == "play":
        game = Game(screen)
        game.run()

    elif action == "quit":
        break

    elif action == "leaderboard":
        menu.show_leaderboard()

    elif action == "settings":
        menu.settings_screen()

pygame.quit()