import pygame
import sys
from ball import Ball

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
ball = Ball(x=WIDTH // 2, y=HEIGHT // 2, radius=25, screen_width=WIDTH, screen_height=HEIGHT
)

done = False

while not done:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        ball.move_left()

    if keys[pygame.K_RIGHT]:
        ball.move_right()

    if keys[pygame.K_UP]:
        ball.move_up()

    if keys[pygame.K_DOWN]:
        ball.move_down()

    pygame.draw.circle(screen, (255, 0, 0), (ball.x, ball.y),ball.radius)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()