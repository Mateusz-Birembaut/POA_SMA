import pygame
from mazelib import Maze as Maze
from mazelib.generate.Prims import Prims


class Labyrinth:
    def __init__(self, size: tuple[int, int]):
        self.__width = size[0] * 2 + 1
        self.__height = size[1] * 2 + 1
        self.__maze = []

        m = Maze()
        m.generator = Prims(size[0], size[1])  # fois 2 + 1
        m.generate()

        m.generate_entrances()
        # m.solver = BacktrackingSolver()
        # m.solve()

        line = ""
        for char in str(m):
            if char != '\n':
                line += char
            else:
                self.__maze.append(line)
                line = ""
        self.__maze.append(line)

    def draw(self, screen: pygame.surface):
        # TODO mettre des marges au labyrinthe

        tile_width = screen.get_width() / self.__width
        tile_height = screen.get_height() / self.__height

        x, y = 0, 0

        for line in self.__maze:
            for tile in line:
                if tile == '#':
                    pygame.draw.rect(screen, "white", (x, y, tile_width, tile_height))
                elif tile == ' ':
                    pygame.draw.rect(screen, (10, 10, 10), (x, y, tile_width, tile_height))

                x += tile_width

            x = 0
            y += tile_height

    def attempt_move(self, position: tuple[int, int]) -> bool:
        # print(position)
        if not self.tile_exists(position): return False
        return self.__maze[position[1]][position[0]] != '#'

    def tile_exists(self, position: tuple[int, int]) -> bool:
        if position[0] < 0 or position[1] < 0: return False
        return not position[1] >= self.__width or position[0] >= self.__height

    def get_tile(self, position: tuple[int, int]) -> str:
        # print(position)
        # for line in self.__maze:
        #     print(line)
        return self.__maze[position[1]][position[0]]

    def set_tile(self, position: tuple[int, int], value: str):
        old_line = self.__maze[position[1]]
        self.__maze[position[1]] = old_line[:position[0]] + value + old_line[position[0]+1:]

    def get_entrance(self) -> tuple[int, int]:
        [print(line) for line in self.__maze]
        for y in range(len(self.__maze)):
            for x in range(len(self.__maze[y])):
                # print(x, y, self.maze[y][x])
                if self.__maze[y][x] == 'E':
                    # print(x, y)
                    return x, y
