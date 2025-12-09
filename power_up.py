import pygame

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, num_sprites, path_sprites, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.path_sprites = path_sprites
        self.num_sprites = num_sprites
        
        for i in range (1, num_sprites+1):
            caminho = self.path_sprites + f'{i}.png'
            img = pygame.transform.scale(pygame.image.load(caminho), (60,40))
            self.sprites.append(img)

        self.ind_sprite = 0
        self.image = self.sprites[0]
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)

    def update(self):
        
        self.ind_sprite += 0.15
        if self.ind_sprite > len(self.sprites):
            self.ind_sprite = 0
        self.image = self.sprites[int(self.ind_sprite)]
