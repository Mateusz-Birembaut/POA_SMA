import numpy

from Entity2 import Entity2
import Scene

class Cat(Entity2):

    def __init__(self, img_url: str, position: tuple[int, int], scene: Scene, maze):
        Entity2.__init__(self, img_url, position, scene, maze)
        self.saw_mouse = False
        self.lastSeenMousePosition = (-1,-1)
        self.runningSpeed = 2

    def seesMouse(self, mouse_position):
        to_test = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for coord in to_test:
            x = self.tile_x + coord[0]
            y = self.tile_y + coord[1]
            while self.maze[y][x] >= 0 :
                if mouse_position == (x, y):
                    self.lastSeenMousePosition = (x,y)
                    self.saw_mouse = True
                    break
                x = x + coord[0]
                y = y + coord[1]

        self.saw_mouse = False

    def move(self, mouse_position):
        self.seesMouse(mouse_position)
        if self.saw_mouse : # si on a vu la souris
            self.moveTowardsLastSeenPosition(mouse_position) # se déplacer vers la position vue
        else :
            #Entity2.move() # avec entity.move => se déplace sur la case la moins visité
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

            self.tile_x += movement[0]
            self.tile_y += movement[1]
            self.maze[self.tile_y][self.tile_x] += 1


    def moveTowardsLastSeenPosition(self, mouse_position):
        x = self.tile_x
        y = self.tile_y
        direction = tuple(numpy.subtract(self.lastSeenMousePosition, (x,y))) #direction vers laquelle la souris a été vu en dernier
        for i in range(self.runningSpeed): # vitesseRunning = nb de cases max par tours
            if abs(direction[0]) > abs(direction[1]):
                x += numpy.sign(direction[0])  # ajoute 1 ou -1 selon la direction
            else:
                y += numpy.sign(direction[1])  # ajoute 1 ou -1 selon la direction

            self.maze[y][x] += 1 # dans le maze de la souris on est passé par la

            if self.lastSeenMousePosition == (x, y) : # si on est arrivé à la dernière position connu on stop
                break

            if mouse_position == (x, y): # si on est sur la souris, cat a gagné
                # ici mettre fin au jeu
                break
        self.tile_x = x
        self.tile_y = y
