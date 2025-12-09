from power_up import PowerUp

class Biblia(PowerUp):
    def __init__(self, pos_x, pos_y):
        super().__init__(num_sprites=7, path_sprites='assets/power-ups/bible/bible', pos_x=pos_x, pos_y=pos_y)
