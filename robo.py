import pygame
from entidade import *
from config import *


# ROBO BASE
class Robo(Entidade):
    def __init__(self, x, y, velocidade):
        super().__init__(x, y, velocidade)
        self.image.fill((255, 0, 0))  # vermelho

    def atualizar_posicao(self):
        raise NotImplementedError


# ROBO EXEMPLO — ZigueZague
class RoboZigueZague(Robo):
    def __init__(self, x, y):
        super().__init__(x, y, velocidade=3)
        self.direcao = 1

    def atualizar_posicao(self):
        self.rect.y += self.velocidade
        self.rect.x += self.direcao * 3

        if self.rect.x <= 0 or self.rect.x >= LARGURA - 40:
            self.direcao *= -1

    def update(self):
        self.atualizar_posicao()
        if self.rect.y > ALTURA:
            self.kill()
