import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
base_layer = pygame.Surface((WIDTH, HEIGHT))

colorRED = (255, 0, 0)

clock = pygame.time.Clock()

LMBpressed = False
THICKNESS = 5

prevX = prevY = 0


def draw_rhombus(surface, x1, y1, x2, y2):
    cx = (x1 + x2) // 2
    cy = (y1 + y2) // 2

    points = [
        (cx, y1), 
        (x2, cy),
        (cx, y2),
        (x1, cy)  
    ]

    pygame.draw.polygon(surface, colorRED, points, THICKNESS)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            LMBpressed = True
            prevX, prevY = event.pos

        if event.type == pygame.MOUSEMOTION:
            screen.blit(base_layer, (0, 0))
            if LMBpressed:
                currX, currY = event.pos
                draw_rhombus(screen, prevX, prevY, currX, currY)

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMBpressed = False
            currX, currY = event.pos
            draw_rhombus(screen, prevX, prevY, currX, currY)
            base_layer.blit(screen, (0, 0))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()