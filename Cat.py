import numpy

import Scene
from Entity import Entity


class Cat(Entity):

    def __init__(self, img_url: str, position: tuple[int, int], scene: Scene, m):
        Entity.__init__(self, img_url, position, scene, m)
        self.saw_mouse = False
        self.lastSeenMousePosition = (-5, -5)
        self.runningSpeed = 2

    def process(self, mouse_position):
        if (self.tile_x, self.tile_y) == mouse_position:
            return
        self.check_mouse(mouse_position)  # regarde si il voit la souris autour
        if self.saw_mouse:  # si on a vu la souris
            self.move_towards_last_seen_position()  # se déplacer vers la position vue
        else:
            super().move()

    def check_mouse(self, mouse_position):
        to_test = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for coord in to_test:
            x = self.tile_x + coord[0]
            y = self.tile_y + coord[1]
            while self.maze[y][x] >= 0:
                if mouse_position == (x, y):
                    self.lastSeenMousePosition = (x, y)
                    self.saw_mouse = True
                    return
                x = x + coord[0]
                y = y + coord[1]
        if self.lastSeenMousePosition != (-5, -5):
            self.saw_mouse = True
            return

        self.saw_mouse = False

    def move_towards_last_seen_position(self):
        x = self.tile_x
        y = self.tile_y
        # direction vers laquelle la souris a été vu en dernier
        direction = tuple(numpy.subtract(self.lastSeenMousePosition, (x, y)))
        for i in range(self.runningSpeed):  # vitesseRunning = nb de cases max par tours
            if abs(direction[0]) > abs(direction[1]):
                x += numpy.sign(direction[0])  # ajoute 1 ou -1 selon la direction
            else:
                y += numpy.sign(direction[1])  # ajoute 1 ou -1 selon la direction

            self.maze[y][x] += 1  # dans le maze du chat on est passé par la

            if self.lastSeenMousePosition == (x, y):  # si on est arrivé à la dernière position connu on stop
                self.lastSeenMousePosition = (-5,-5)
                break

        self.tile_x = x
        self.tile_y = y
