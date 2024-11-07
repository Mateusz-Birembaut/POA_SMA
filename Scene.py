class Scene:

    def __init__(self, tile_nb: tuple[int, int], tile_px: tuple[int, int], margin_right):
        self.tile_width = tile_nb[0] * 2 + 1
        self.tile_height = tile_nb[1] * 2 + 1
        self.tile_width_px = tile_px[0]
        self.tile_height_px = tile_px[1]
        self.screen_width = self.tile_width * tile_px[0] + margin_right
        self.screen_height = self.tile_height * tile_px[1]
        self.margin_right = margin_right
