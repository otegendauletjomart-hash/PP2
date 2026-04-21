import pygame

pygame.init()
done = False
surface = pygame.display.set_mode((400, 300))

# pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(100, 150, 100, 60))

# pygame.draw.circle(screen, (0, 128, 255), (100, 100), (50))

# draw a rectangle
pygame.draw.rect(surface, (0, 128, 255), pygame.Rect(10, 10, 100, 100), 10)
# draw a circle
pygame.draw.circle(surface, (0, 128, 255), (300, 60), 50, 10)

pygame.draw.polygon(surface, (255, 200, 0), [
    (250, 200),
    (270, 230),
    (300, 240),
    (270, 260),
    (250, 300),
    (230, 260),
    (200, 240),
    (230, 230)
])

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()
