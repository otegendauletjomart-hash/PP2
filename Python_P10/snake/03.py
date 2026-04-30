import pygame
from color_palette import *
import random

pygame.init()

WIDTH = 600
HEIGHT = 600
CELL = 30

screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont("Arial", 24)

# ===== GAME SETTINGS =====
base_FPS = 5
FPS = base_FPS

score = 0
level = 1
foods_eaten = 0
FOOD_PER_LEVEL = 5


def draw_grid():
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colorGRAY,
                             (i * CELL, j * CELL, CELL, CELL), 1)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0

    def change_direction(self, new_dx, new_dy):
        # 🚫 запрет разворота
        if (self.dx == 1 and new_dx == -1) or \
           (self.dx == -1 and new_dx == 1) or \
           (self.dy == 1 and new_dy == -1) or \
           (self.dy == -1 and new_dy == 1):
            return

        self.dx = new_dx
        self.dy = new_dy

    def get_next_head(self):
        return Point(
            self.body[0].x + self.dx,
            self.body[0].y + self.dy
        )

    def will_collide(self):
        next_head = self.get_next_head()

        # стены
        if (next_head.x < 0 or next_head.x >= WIDTH // CELL or
            next_head.y < 0 or next_head.y >= HEIGHT // CELL):
            return True

        # тело
        for s in self.body:
            if next_head.x == s.x and next_head.y == s.y:
                return True

        return False

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def draw(self):
        head = self.body[0]

        pygame.draw.rect(screen, colorRED,
                         (head.x * CELL, head.y * CELL, CELL, CELL))

        for s in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW,
                             (s.x * CELL, s.y * CELL, CELL, CELL))

    def eat(self, food):
        global score, foods_eaten

        head = self.body[0]

        if head.x == food.pos.x and head.y == food.pos.y:
            score += food.weight
            foods_eaten += 1

            for _ in range(food.weight):
                self.body.append(Point(head.x, head.y))

            food.generate_random_pos(self)
            return True

        return False


class Food:
    def __init__(self):
        self.pos = Point(9, 9)
        self.weight = random.choice([1, 2, 3])

        # 🎯 FIXED TIMER = 60 TICKS ALWAYS
        self.max_timer = 60
        self.timer = self.max_timer

    def generate_random_pos(self, snake):
        while True:
            x = random.randint(0, WIDTH // CELL - 1)
            y = random.randint(0, HEIGHT // CELL - 1)

            collision = False
            for s in snake.body:
                if s.x == x and s.y == y:
                    collision = True
                    break

            if not collision:
                self.pos.x = x
                self.pos.y = y
                break

        self.weight = random.choice([1, 2, 3])

        # reset timer to FIXED 60
        self.timer = self.max_timer

    def update(self):
        self.timer -= 1
        if self.timer <= 0:
            self.generate_random_pos(snake)

    def draw(self):
        if self.weight == 1:
            color = colorGREEN
        elif self.weight == 2:
            color = colorYELLOW
        else:
            color = colorRED

        # shrinking effect
        size = CELL
        if self.timer < 40:
            size = CELL - 8
        if self.timer < 20:
            size = CELL - 14

        offset = (CELL - size) // 2

        pygame.draw.rect(
            screen,
            color,
            (self.pos.x * CELL + offset,
             self.pos.y * CELL + offset,
             size, size)
        )


# ===== INIT =====
clock = pygame.time.Clock()
snake = Snake()
food = Food()
food.generate_random_pos(snake)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.change_direction(1, 0)
            elif event.key == pygame.K_LEFT:
                snake.change_direction(-1, 0)
            elif event.key == pygame.K_DOWN:
                snake.change_direction(0, 1)
            elif event.key == pygame.K_UP:
                snake.change_direction(0, -1)

    screen.fill(colorBLACK)
    draw_grid()

    # 💀 collision BEFORE move (precise hitbox logic)
    if snake.will_collide():
        print("Game Over!")
        running = False
    else:
        snake.move()

    snake.eat(food)
    food.update()

    # LEVEL SYSTEM
    level = foods_eaten // FOOD_PER_LEVEL + 1
    FPS = base_FPS + (level - 1)

    snake.draw()
    food.draw()

    # HUD
    text1 = font.render(f"Score: {score}  Level: {level}", True, colorWHITE)
    screen.blit(text1, (10, 10))

    timer_text = font.render(
        f"Food disappears in: {food.timer}/{food.max_timer}",
        True,
        colorWHITE
    )
    screen.blit(timer_text, (10, 40))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()