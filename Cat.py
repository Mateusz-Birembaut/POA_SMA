import numpy

from Entity import Entity
import Scene

class Cat(Entity):

    def __init__(self, img_url: str, position: tuple[int, int], scene: Scene, maze):
        Entity.__init__(self, img_url, position, scene, maze)
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
                    return
                x = x + coord[0]
                y = y + coord[1]

        self.saw_mouse = False

    def move(self, mouse_position):
        self.seesMouse(mouse_position) # regarde si il voit la souris autour
        if self.saw_mouse : # si on a vu la souris
            self.moveTowardsLastSeenPosition(mouse_position) # se déplacer vers la position vue
        else :
            # se déplace sur la case la moins visité autour
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
