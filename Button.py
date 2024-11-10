class Button:
    def __init__(self, text, pos, font, color=(0, 0, 0)):
        self.text = text
        self.pos = pos
        self.font = font
        self.color = color
        self.rendered_text = self.font.render(self.text, True, self.color)
        self.rect = self.rendered_text.get_rect(center=self.pos)

    def draw(self, surface):
        surface.blit(self.rendered_text, self.rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
