import random

import pygame
from mazelib import Maze as Maze
from mazelib.generate.Prims import Prims


class Labyrinth:
    def __init__(self, size: tuple[int, int]):
        self.__width = size[0] * 2 + 1
        self.__height = size[1] * 2 + 1
        self.__maze = []
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
                line += char
            else:
                self.__maze.append(line)
                line = ''
        self.__maze.append(line)

    def draw(self, screen: pygame.surface, margin_right):
        drawable_width = screen.get_width() - margin_right

        tile_width = drawable_width / self.__width
        tile_height = drawable_width / self.__height

        x, y = 0, 0

        for line in self.__maze:
            for tile in line:
                if tile == '#':
                    pygame.draw.rect(screen, "white", (x, y, tile_width, tile_height))
                elif tile == ' ':
                    pygame.draw.rect(screen, (0, 0, 0), (x, y, tile_width, tile_height))
                elif tile == 'E':
                    pygame.draw.rect(screen, (127, 127, 127), (x, y, tile_width, tile_height))
                    self.exits.append((x / tile_width, y / tile_height))
                elif tile == 'S':
                    pygame.draw.rect(screen, (0, 255, 0), (x, y, tile_width, tile_height))
                    self.exits.append((x / tile_width, y / tile_height))

                x += tile_width

            x = 0
            y += tile_height

    def get_random_empty_position(self):
        while True:
            x = random.randint(0, self.__width - 1)
            y = random.randint(0, self.__height - 1)
            if self.__maze[y][x] == ' ':
                return x, y

    def attempt_move(self, position: tuple[int, int]) -> bool:
        # todo calculer la position
        # todo vérifier si ya pas le chat/souris
        if not self.__tile_exists(position): return False
        return self.__maze[position[1]][position[0]] != '#'

    def __tile_exists(self, position: tuple[int, int]) -> bool:
        if position[0] < 0 or position[1] < 0: return False
        return not (position[0] >= self.__width or position[1] >= self.__height)

    def get_tile(self, position: tuple[int, int]) -> str:
        if not self.__tile_exists(position): return ''
        return self.__maze[position[1]][position[0]]

    def set_tile(self, position: tuple[int, int], value: str):
        if not self.__tile_exists(position): return
        old_line = self.__maze[position[1]]
        self.__maze[position[1]] = old_line[:position[0]] + value + old_line[position[0]+1:]

    def get_entrance(self) -> tuple[int, int]:
        [print(line) for line in self.__maze]
        for y in range(len(self.__maze)):
            for x in range(len(self.__maze[y])):
                if self.__maze[y][x] == 'E':
                    return x, y
