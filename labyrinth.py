from mazelib import Maze as mz
from mazelib.generate.Prims import Prims
from mazelib.solve.BacktrackingSolver import BacktrackingSolver
import pygame

class Maze:
    def __init__(self, size: tuple[int,int]):
        self.width = size[0] * 2 + 1
        self.height = size[1] * 2 + 1

        m = mz()
        m.generator = Prims(size[0], size[1])  # fois 2 + 1
        m.generate()

        m.generate_entrances()
        # m.solver = BacktrackingSolver()
        # m.solve()

        self.maze = str(m)

    def draw(self, screen: pygame.surface):
        # TODO mettre des marges au labyrinthe

        tile_width = screen.get_width() / self.width
        tile_height = screen.get_height() / self.height

        x, y = 0, 0

        for tile in self.maze:
            if tile == '#':
                pygame.draw.rect(screen, (255, 255, 255), (x, y, tile_width, tile_height))
            elif tile == ' ':
                pygame.draw.rect(screen, (10, 10, 10), (x, y, tile_width, tile_height))
            
            x += tile_width

            if tile == '\n':
                x = 0
                y += tile_height
