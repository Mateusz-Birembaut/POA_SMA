import pygame
from mazelib import Maze as Mz
from mazelib.generate.Prims import Prims


class Maze:
    def __init__(self, width: int, height: int):
        self.width = width * 2 + 1
        self.height = height * 2 + 1
        self.maze = []

        m = Mz()
        m.generator = Prims(width, height)  # fois 2 + 1
        m.generate()

        m.generate_entrances()
        # m.solver = BacktrackingSolver()
        # m.solve()

        line = ""
        for char in str(m):
            if char != '\n':
                line += char
            else:
                self.maze.append(line)
                line = ""
        self.maze.append(line)

    def draw(self, screen: pygame.surface):
        # TODO mettre des marges au labyrinthe

        tile_width = screen.get_width() / self.width
        tile_height = screen.get_height() / self.height

        x, y = 0, 0

        for line in self.maze:
            for tile in line:
                if tile == '#':
                    pygame.draw.rect(screen, "white", (x, y, tile_width, tile_height))
                elif tile == ' ':
                    pygame.draw.rect(screen, (10, 10, 10), (x, y, tile_width, tile_height))

                x += tile_width

            x = 0
            y += tile_height
