import pygame
import sys
import random

pygame.init()

# Game constants
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20
CELL_SIZE = WIDTH // GRID_SIZE
FPS = 10

# Colors
WHITE = (255, 255 ,255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
DARK_BLUE = (0, 0, 139)
GRAY = (90,90,90)
BLACK = (0, 0 ,0)

snake = [(GRID_SIZE // 2, GRID_SIZE // 2)]
food = None

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        for y in range(0, HEIGHT, CELL_SIZE):
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GRAY, rect, 1)

def draw_snake():
    for i, cell in enumerate(snake):
        rect = pygame.Rect(cell[0]*CELL_SIZE, cell[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE)
        if i == 0:
            pygame.draw.rect(screen, DARK_BLUE, rect)
        else:
            pygame.draw.rect(screen, BLUE, rect)

def draw_food():
    if food:
        rect = pygame.Rect(food[0]*CELL_SIZE, food[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, RED, rect)

def check_food():
    global food
    if not food:
        food = (random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1))
        if food in snake:
            food = None

def update_snake():
    global snake, food
    head = snake[0]
    new_head = ((head[0] + dx) % GRID_SIZE, (head[1] + dy) % GRID_SIZE)

    if new_head in snake:
        return False

    snake.insert(0, new_head)
    if food and new_head == food:
        food = None
    else:
        snake.pop()

    return True

dx, dy = 1, 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and dy == 0:
                dx, dy = 0, -1
            elif event.key == pygame.K_s and dy == 0:
                dx, dy = 0, 1
            elif event.key == pygame.K_a and dx == 0:
                dx, dy = -1, 0
            elif event.key == pygame.K_d and dx == 0:
                dx, dy = 1, 0

    screen.fill(BLACK)

    if not update_snake():
        break

    check_food()

    draw_grid()
    draw_snake()
    draw_food()

    pygame.display.flip()
    clock.tick(FPS)
