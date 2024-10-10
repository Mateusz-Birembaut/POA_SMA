class Scene:

    def __init__(self, tile_nb, tile_px):
        self.tile_width = tile_nb[0] * 2 + 1
        self.tile_height = tile_nb[1] * 2 + 1
        self.tile_width_px = tile_px[0]
        self.tile_height_px = tile_px[1]
        self.screen_width = tile_nb[0] * tile_px[0]
        self.screen_height = tile_nb[1] * tile_px[1]
        print(tile_nb)
