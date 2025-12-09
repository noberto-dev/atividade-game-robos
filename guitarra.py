from power_up import PowerUp

class Guitarra(PowerUp):
    def __init__(self, pos_x, pos_y):
        super().__init__(num_sprites=6, path_sprites='assets/power-ups/guitarra/guitar', pos_x=pos_x, pos_y=pos_y)
        
