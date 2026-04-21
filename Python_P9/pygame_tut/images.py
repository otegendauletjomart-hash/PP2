import pygame

pygame.init()

screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

done = False

surface = pygame.Surface((100, 100))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True 

pygame.quit()