import numpy

from Entity2 import Entity2
import Scene

class Cat(Entity2):

    def __init__(self, img_url: str, position: tuple[int, int], scene: Scene, maze):
        Entity2.__init__(self, img_url, position, scene, maze)
        self.sawMouse = False
        self.lastSeenMousePosition = (-1,-1)
        self.runningSpeed = 2

    def seesMouse(self, mousePosition):
        to_test = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for coord in to_test:
            x = self.tile_x + coord[0]
            y =  self.tile_y + coord[1]
            while(self.maze[x][y] >= 0):
                if mousePosition == (x, y):
                    self.lastSeenMouse = (x,y)
                    self.sawMouse = True
                    break
                x = x + coord[0]
                y = y + coord[1]

        self.sawMouse = False

    def move(self, mousePosition):
        self.seesMouse(mousePosition)
        if(self.sawMouse == True): # si on a vu la souris
            self.moveTowardsLastSeenPosition(mousePosition) # se déplacer vers la position vue
        else :
            #Entity2.move() # avec entity.move => se déplace sur la case la moins visité
            print("cat x :" ,self.tile_x)
            print("cat y :" ,self.tile_y)

            print("indice de la case x-1 :" ,self.maze[self.tile_x-1][self.tile_y])
            print("indice de la case x+1 :" ,self.maze[self.tile_x+1][self.tile_y])
            print("indice de la case y-1 :" ,self.maze[self.tile_x][self.tile_y]-1)
            print("indice de la case y+1 :" ,self.maze[self.tile_x][self.tile_y]+1)

            to_test = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            smallestIndex = 1000;
            movement = [0,0]
            x = self.tile_x
            y = self.tile_y
            for coord in to_test:
                x = x + coord[0]
                y = y + coord[1]
                tileIndex = self.maze[y][x]
                if(tileIndex >= 0):
                    if(tileIndex < smallestIndex):
                        smallestIndex = tileIndex
                        movement = coord
            self.tile_x = self.tile_x + movement[0]
            self.tile_y = self.tile_y + movement[1]
            self.maze[self.tile_x][self.tile_y] += 1


    def moveTowardsLastSeenPosition(self, mousePosition):
        x = self.tile_x
        y = self.tile_y
        direction = tuple(numpy.subtract(self.lastSeenMousePosition, (x,y))) #direction vers laquelle la souris a été vu en dernier
        for i in range(self.runningSpeed): # vitesseRunning = nb de cases max par tours
            if abs(direction[0]) > abs(direction[1]):
                x += numpy.sign(direction[0])  # ajoute 1 ou -1 selon la direction
            else:
                y += numpy.sign(direction[1])  # ajoute 1 ou -1 selon la direction

            self.labyrinth.maze[y][x] += 1 # dans le maze de la souris on est passé par la

            if(self.lastSeenMousePosition == (x,y)): # si on est arrivé à la dernière position connu on stop
                break

            if(mousePosition == (x,y)): ## si on est sur la souris, cat a gagné
                # ici mettre fin au jeu
                break
        self.tuple_x = x
        self.tuple_y = y
