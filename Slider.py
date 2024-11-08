import pygame


class Slider:
    def __init__(self, text, font, x, y, width, height, min_val, max_val, initial_val):
        self.rect = pygame.Rect(x, y, width, height)
        self.min_val = min_val
        self.max_val = max_val
        self.value = initial_val

        self.font = font
        self.text = text
        self.text_surface = self.font.render(self.text, True, (0, 0, 0))
        
        self.handle_rect = pygame.Rect(
            x + (width * (initial_val - min_val) / (max_val - min_val)) - 5, 
            y - 5, 10, height + 10)
        self.dragging = False

    def draw(self, surface):
        pygame.draw.rect(surface, (200, 200, 200), self.rect)  # slider
        pygame.draw.rect(surface, (100, 100, 100), self.handle_rect)  # barre du slider
        surface.blit(self.text_surface, (self.rect.x, self.rect.y - 50))  # texte du slider

        value_surface = self.font.render(str(int(self.value)), True, (0, 0, 0)) # texte de la valeur du slider
        surface.blit(value_surface, (self.rect.x + self.rect.width / 2 - 14, self.rect.y - 30))

    def is_clicked(self, mouse_pos):
        return self.handle_rect.collidepoint(mouse_pos)


    