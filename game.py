import sys
import pygame
from pygame.locals import *

from labyrinth import Maze

pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

width, height = 1600, 900
screen = pygame.display.set_mode((width, height))

labyrinthe = Maze((10, 10))

mouse_image = pygame.image.load("./res/mouse.png").convert_alpha()

# Game loop.
while True:
  screen.fill((0, 0, 0))

  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

  # Update.

  # Draw.
  labyrinthe.draw(screen)
  screen.blit(mouse_image, mouse_image.get_rect(center = screen.get_rect().center))

  pygame.display.flip()
  fpsClock.tick(fps)
