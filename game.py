import random
import sys

import pygame
from pygame.locals import *

from Entity import Entity
from Labyrinth import Labyrinth
from Scene import Scene

pygame.init()
gameClock = pygame.time.Clock()

tile_width, tile_height = 10, 10
tile_width_px, tile_height_px = 35, 35

scene = Scene((tile_width, tile_height), (tile_width_px, tile_height_px))

screen = pygame.display.set_mode((scene.screen_width, scene.screen_height))

labyrinth = Labyrinth((tile_width, tile_height))

mouse_x, mouse_y = 0, 0
mouse = Entity('./res/mouse.png', (mouse_x, mouse_y), scene, labyrinth, 'mouse')

cat_x, cat_y = 1, 1
cat = Entity('./res/cat.png', (cat_x, cat_y), scene, labyrinth, 'cat')


# Game loop
while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Update
    pygame.time.wait(50)
    mouse_x += (-1 if mouse_x == 20 else 1) * int(random.random()*2)
    mouse_y += (-1 if mouse_y == 20 else 1) * int(random.random()*2)

    # Draw
    labyrinth.draw(screen)
    mouse.move((mouse_x, mouse_y))
    mouse.draw(screen,)
    cat.move((cat_x, cat_y))
    cat.draw(screen)

    pygame.display.flip()
    gameClock.tick(30)
