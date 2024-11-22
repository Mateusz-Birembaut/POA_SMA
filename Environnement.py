import random

import pygame
from mazelib import Maze as Maze
from mazelib.generate.Prims import Prims


class Environnement:
    def __init__(self, size: tuple[int, int]):
        self.__width = size[0] * 2 + 1
        self.__height = size[1] * 2 + 1
        self.__maze = []

        m = Maze()
        m.generator = Prims(size[0], size[1])  # fois 2 + 1
        m.generate()

        m.generate_entrances()
        self.m = m

        line = ''
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
                elif tile == 'S':
                    pygame.draw.rect(screen, (0, 255, 0), (x, y, tile_width, tile_height))

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
        tile = self.get_tile(position)
        if tile == '': return False # '' est une case inexistante donc on renvoit faux
        return tile != '#'

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

    def change_agent_pos(self, new_position: tuple[int, int], agent_symbol: str):
        old_position = self.get_position_of(agent_symbol)
        if old_position:
            self.set_tile(old_position, ' ')
        if not new_position == self.get_position_of('S'):
            self.set_tile(new_position, agent_symbol)

    def get_position_of(self, target: str) -> tuple[int, int]:
        for y in range(len(self.__maze)):
            for x in range(len(self.__maze[y])):
                if self.__maze[y][x] == target:
                    return x, y
