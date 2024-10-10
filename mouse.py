import pygame

class Mouse:

    def __init__(self, size, position):
        self.position = position
        self.width = size[0]
        self.height = size[1]

    def draw(self, screen):
        IMAGE = pygame.image.load('./res/mouse.png').convert_alpha()
        IMAGE = pygame.transform.scale(IMAGE, (self.width ,self.height))
        screen.blit(IMAGE, self.position)
        
