import pygame
from mazelib import Maze as Maze
from mazelib.generate.Prims import Prims


class Labyrinth:
    def __init__(self, size: tuple[int, int]):
        self.width = size[0] * 2 + 1
        self.height = size[1] * 2 + 1
        self.maze = []

        m = Maze()
        m.generator = Prims(size[0], size[1])  # fois 2 + 1
        m.generate()

        m.generate_entrances()
        # m.solver = BacktrackingSolver()
        # m.solve()

        line = []
        for char in str(m):
            if char != '\n':
                integer = 0
                if char == '#':
                    integer = -1
                elif char == 'E':
                    integer = -2
                elif char == 'S':
                    integer = -3
                line.append(integer)
            else:
                self.maze.append(line)
                line = []
        self.maze.append(line)

    def draw(self, screen: pygame.surface):
        # TODO mettre des marges au labyrinthe

        tile_width = screen.get_width() / self.width
        tile_height = screen.get_height() / self.height

        x, y = 0, 0

        for line in self.maze:
            for tile in line:
                if tile == -1:
                    pygame.draw.rect(screen, "white", (x, y, tile_width, tile_height))
                else :
                    pygame.draw.rect(screen, (10, 10, 10), (x, y, tile_width, tile_height))

                x += tile_width

            x = 0
            y += tile_height
