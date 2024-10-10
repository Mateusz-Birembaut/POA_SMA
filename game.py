import sys
import pygame
from pygame.locals import *

from mouse import Mouse
from labyrinth import Maze

pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

tile_x, tile_y = 10, 10
tile_width, tile_height = 35, 35

width, height = (tile_x*2+1)*tile_width, (tile_y*2+1)*tile_height
screen = pygame.display.set_mode((width, height))

labyrinthe = Maze(tile_x, tile_y)

mouse = Mouse((tile_width,tile_height),pygame.Vector2(width/2,height/2))

# Game loop
while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Update

    # Draw
    labyrinthe.draw(screen)
    mouse.draw(screen)


    pygame.display.flip()
    fpsClock.tick(fps)
