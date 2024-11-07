import pygame

import Scene


class Entity:

    def __init__(self, img_url: str, position: tuple[int, int], scene: Scene, maze):
        self.image = pygame.image.load(img_url).convert_alpha()
        self.image = pygame.transform.scale(self.image, (scene.tile_width_px, scene.tile_height_px))
        self.tile_x = position[0]
        self.tile_y = position[1]
        self.scene = scene
        self.maze = maze
        self.maze[self.tile_x][self.tile_y] = 1

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.tile_x * self.scene.tile_width_px, self.tile_y * self.scene.tile_height_px))


    def move(self):
        to_test = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        smallest_index = 1000
        movement = [0, 0]
        for coord in to_test:
            x = self.tile_x + coord[0]
            y = self.tile_y + coord[1]
            tile_index = self.maze[y][x]
            if 0 <= tile_index < smallest_index:
                smallest_index = tile_index
                movement = coord

        self.maze[self.tile_y][self.tile_x] += 1

        self.tile_x += movement[0]
        self.tile_y += movement[1]

        self.checkIfDeadEnd()

    def checkIfDeadEnd(self):
        to_test = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for coord in to_test:
            foundWall = False
            i = 1  # commence a 1 pour tester les cases adjacentes
            while not foundWall:
                x = self.tile_x + coord[0] * i
                y = self.tile_y + coord[1] * i

                # si que (x, y) est dans les limites
                if 0 <= x < len(self.maze[0]) and 0 <= y < len(self.maze):
                    tile_index = self.maze[y][x]

                    if tile_index == -1:  # si un mur est trouvé
                        foundWall = True
                        isDeadEnd = True
                        index = 1
                        while index < i:
                            x = self.tile_x + coord[0] * index
                            y = self.tile_y + coord[1] * index

                            if 0 <= x < len(self.maze[0]) and 0 <= y < len(self.maze):

                                # Verifie les cases adjactentes pour verifier si c'est un couloir

                                if coord[0] != 0:  # check les cases en focntion de si on est dans un mvt horizontale ou vertical
                                    if (y + 1 < len(self.maze) and self.maze[y + 1][x] != -1) or \
                                            (y - 1 >= 0 and self.maze[y - 1][x] != -1):
                                        isDeadEnd = False
                                        break
                                else:
                                    if (x + 1 < len(self.maze[0]) and self.maze[y][x + 1] != -1) or \
                                            (x - 1 >= 0 and self.maze[y][x - 1] != -1):
                                        isDeadEnd = False
                                        break

                            index += 1

                        # si ce couloir est un cul de sac, j'incrémente les valeurs de ce chemin de +10 pour pas y passer
                        if isDeadEnd:
                            index = 1
                            while index < i:
                                x = self.tile_x + coord[0] * index
                                y = self.tile_y + coord[1] * index
                                self.maze[y][x] += 10
                                index += 1
                else:
                    break  # si on est hors limite on dit que non

                i += 1