import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 800
FPS = 60
PLAYER_SPEED = 3
player = pygame.Rect((400,400, 20, 20))
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

MOVEMENT_KEYS = {
    pygame.K_w: (0, -PLAYER_SPEED),
    pygame.K_s: (0, PLAYER_SPEED),
    pygame.K_a: (-PLAYER_SPEED, 0),
    pygame.K_d: (PLAYER_SPEED, 0),
}

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    key = pygame.key.get_pressed()
    for movement_key, movement_vector in MOVEMENT_KEYS.items():
        if key[movement_key]:
            player.move_ip(movement_vector)

    if player.left < 0: player.left = 0
    if player.right > WIDTH: player.right = WIDTH
    if player.top < 0: player.top = 0
    if player.bottom > HEIGHT: player.bottom = HEIGHT

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), player)

    pygame.display.flip()

    clock.tick(FPS)
