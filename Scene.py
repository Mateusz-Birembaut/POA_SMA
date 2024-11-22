import Environnement


class Scene:

    def __init__(self, tile_nb: tuple[int, int], tile_px: tuple[int, int], margin_right: int):
        self.tile_width_nb = tile_nb[0] * 2 + 1
        self.tile_height_nb = tile_nb[1] * 2 + 1
        self.tile_width_px = tile_px[0]
        self.tile_height_px = tile_px[1]
        self.screen_width = self.tile_width_nb * tile_px[0] + margin_right
        self.screen_height = self.tile_height_nb * tile_px[1]
        self.margin_right = margin_right
        self.lab = None

    def set_environnement(self, lab: Environnement):
        self.lab = lab
