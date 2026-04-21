import pygame
import sys
import os
from player import Player

pygame.init()

WIDTH, HEIGHT = 500, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

font = pygame.font.Font(None, 36)

music_folder = "music"

playlist = [
    os.path.join(music_folder, file)
    for file in os.listdir(music_folder)
    if file.endswith((".wav", ".mp3", ".ogg"))
]

playlist.sort()

player = Player(playlist)

clock = pygame.time.Clock()

done = False

while not done:
    screen.fill((20, 20, 20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_q:
                running = True

            elif event.key == pygame.K_p:
                player.play()

            elif event.key == pygame.K_s:
                player.stop()

            elif event.key == pygame.K_n:
                player.next()

            elif event.key == pygame.K_b:
                player.previous()

    track_name = player.get_current_track() if playlist else "No music"

    screen.blit(font.render(f"Track: {track_name}", True, (255, 255, 255)), (20, 50))

    status = "Playing" if player.is_playing else "Stopped"
    screen.blit(font.render(status, True, (0, 255, 0)), (20, 100))

    screen.blit(font.render("P Play | S Stop | N Next | B Back | Q Quit", True, (200, 200, 200)), (20, 200))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()