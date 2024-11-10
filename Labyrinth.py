import random

import pygame
from mazelib import Maze as Maze
from mazelib.generate.Prims import Prims


class Labyrinth:
    def __init__(self, size: tuple[int, int]):
        self.width = size[0] * 2 + 1
        self.height = size[1] * 2 + 1
        self.maze_num = []
        self.maze = []
        self.exits = []

        m = Maze()
        m.generator = Prims(size[0], size[1])  # fois 2 + 1
        m.generate()

        m.generate_entrances()
        # m.solver = BacktrackingSolver()
        # m.solve()
        self.m = m

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
                self.maze_num.append(line)
                line = []
        self.maze_num.append(line)

    def draw(self, screen: pygame.surface, margin_right):
        drawable_width = screen.get_width() - margin_right

        tile_width = drawable_width / self.width
        tile_height = drawable_width / self.height 

        x, y = 0, 0

        for line in self.maze_num:
            for tile in line:
                if tile == -1:
                    pygame.draw.rect(screen, "white", (x, y, tile_width, tile_height))
                elif tile == -2:
                    pygame.draw.rect(screen, "red", (x, y, tile_width, tile_height))
                    self.exits.append((x / tile_width, y / tile_height))
                elif tile == -3:
                    pygame.draw.rect(screen, "green", (x, y, tile_width, tile_height))
                    self.exits.append((x / tile_width, y / tile_height))
                else:
                    pygame.draw.rect(screen, (10, 10, 10), (x, y, tile_width, tile_height))

                x += tile_width

            x = 0
            y += tile_height

    def get_random_empty_position(self):
        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if self.maze_num[y][x] >= 0:
                return x, y
