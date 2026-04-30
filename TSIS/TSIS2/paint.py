import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
base_layer = pygame.Surface((WIDTH, HEIGHT))

clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

color = WHITE

THICKNESS = 5

font = pygame.font.SysFont("Arial", 24)

def set_brush_size(size):
    global THICKNESS
    THICKNESS = size

mode = 1

LMBpressed = False
startX = startY = 0
currX = currY = 0

text_mode = False
text_x = 0
text_y = 0
text_input = ""

def flood_fill(surface, x, y, target_color, replacement_color):
    if target_color == replacement_color:
        return

    width, height = surface.get_size()
    stack = [(x, y)]

    while stack:
        cx, cy = stack.pop()

        if cx < 0 or cx >= width or cy < 0 or cy >= height:
            continue

        current_color = surface.get_at((cx, cy))[:3]

        if current_color != target_color:
            continue

        surface.set_at((cx, cy), replacement_color)

        stack.append((cx + 1, cy))
        stack.append((cx - 1, cy))
        stack.append((cx, cy + 1))
        stack.append((cx, cy - 1))

def draw_line(surf, x1, y1, x2, y2):
    pygame.draw.line(surf, color, (x1, y1), (x2, y2), THICKNESS)

def draw_square(surf, x1, y1, x2, y2):
    size = max(abs(x2 - x1), abs(y2 - y1))
    rect = pygame.Rect(x1, y1, size, size)
    pygame.draw.rect(surf, color, rect, THICKNESS)

def draw_triangle(surf, x1, y1, x2, y2):
    side = abs(x2 - x1)
    h = int((3 ** 0.5 / 2) * side)

    points = [
        (x1, y1),
        (x1 + side, y1),
        (x1 + side // 2, y1 - h)
    ]
    pygame.draw.polygon(surf, color, points, THICKNESS)

def draw_rhombus(surf, x1, y1, x2, y2):
    cx = (x1 + x2) // 2
    cy = (y1 + y2) // 2

    points = [
        (cx, y1),
        (x2, cy),
        (cx, y2),
        (x1, cy)
    ]
    pygame.draw.polygon(surf, color, points, THICKNESS)

def draw_right_triangle(surf, x1, y1, x2, y2):
    points = [(x1, y1), (x2, y2), (x1, y2)]
    pygame.draw.polygon(surf, color, points, THICKNESS)

running = True

while running:

    screen.fill(BLACK)
    screen.blit(base_layer, (0, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_1:
                mode = 1
            elif event.key == pygame.K_2:
                mode = 2
            elif event.key == pygame.K_3:
                mode = 3
            elif event.key == pygame.K_4:
                mode = 4
            elif event.key == pygame.K_5:
                mode = 5
            elif event.key == pygame.K_6:
                mode = 6
            elif event.key == pygame.K_7:
                mode = 7
            elif event.key == pygame.K_8:
                mode = 8
            elif event.key == pygame.K_9:
                mode = 9
                text_mode = False

            elif event.key == pygame.K_q:
                color = WHITE
            elif event.key == pygame.K_w:
                color = BLACK
            elif event.key == pygame.K_e:
                color = RED
            elif event.key == pygame.K_r:
                color = GREEN
            elif event.key == pygame.K_t:
                color = BLUE
            elif event.key == pygame.K_y:
                color = YELLOW

            elif event.key == pygame.K_a:
                set_brush_size(2)
            elif event.key == pygame.K_s:
                set_brush_size(5)
            elif event.key == pygame.K_d:
                set_brush_size(10)

            elif event.key == pygame.K_c:
                base_layer.fill(BLACK)

            if mode == 9 and text_mode:

                if event.key == pygame.K_RETURN:
                    base_layer.blit(font.render(text_input, True, color), (text_x, text_y))
                    text_mode = False
                    text_input = ""

                elif event.key == pygame.K_ESCAPE:
                    text_mode = False
                    text_input = ""

                elif event.key == pygame.K_BACKSPACE:
                    text_input = text_input[:-1]

                else:
                    text_input += event.unicode

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            LMBpressed = True
            startX, startY = event.pos

            if mode == 8:
                target = base_layer.get_at((startX, startY))[:3]
                flood_fill(base_layer, startX, startY, target, color)

            if mode == 9:
                text_mode = True
                text_x, text_y = event.pos
                text_input = ""

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMBpressed = False
            currX, currY = event.pos

            if mode == 3:
                draw_line(base_layer, startX, startY, currX, currY)
            elif mode == 4:
                draw_square(base_layer, startX, startY, currX, currY)
            elif mode == 5:
                draw_triangle(base_layer, startX, startY, currX, currY)
            elif mode == 6:
                draw_rhombus(base_layer, startX, startY, currX, currY)
            elif mode == 7:
                draw_right_triangle(base_layer, startX, startY, currX, currY)

        if event.type == pygame.MOUSEMOTION and LMBpressed:

            currX, currY = event.pos

            if mode == 1:
                pygame.draw.line(base_layer, color,
                                 (startX, startY), (currX, currY), THICKNESS)
                startX, startY = currX, currY

            elif mode == 2:
                pygame.draw.line(base_layer, BLACK,
                                 (startX, startY), (currX, currY), THICKNESS)
                startX, startY = currX, currY

            else:
                temp = base_layer.copy()

                if mode == 3:
                    draw_line(temp, startX, startY, currX, currY)
                elif mode == 4:
                    draw_square(temp, startX, startY, currX, currY)
                elif mode == 5:
                    draw_triangle(temp, startX, startY, currX, currY)
                elif mode == 6:
                    draw_rhombus(temp, startX, startY, currX, currY)
                elif mode == 7:
                    draw_right_triangle(temp, startX, startY, currX, currY)

                screen.blit(temp, (0, 0))

    if text_mode:
        preview = font.render(text_input, True, color)
        screen.blit(preview, (text_x, text_y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()