import numpy

from Entity import Entity

class Cat(Entity):

    def __init__(self, img_url: str, position: tuple[int, int], scene: Scene, labyrinth: Labyrinth, name: str):
        Entity.__init__(img_url, position, scene, labyrinth, name)
        self.sawMouse = False
        self.lastSeenMousePosition = (-1,-1)
        self.runningSpeed = 2

    def seesMouse(self, mousePosition):
        to_test = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for coord in to_test:
            x = self.tile_x + coord[0]
            y =  self.tile_y + coord[1]
            while(self.labyrinth.maze[y][x] != '#'):
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
            Entity.move() # avec entity.move => se déplace sur la case la moins visité


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
