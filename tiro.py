import pygame
from entidade import *


class Tiro(Entidade):
    def __init__(self, x, y):
        super().__init__(x + 43, y, 10)
        self.image = pygame.image.load("atividade-game-robos-main/assets/tiro.png")
        self.image = pygame.transform.scale(self.image, (20,20))

    def update(self):
        self.rect.y -= self.velocidade
        if self.rect.y < 0:
            self.kill()

