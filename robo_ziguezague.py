import pygame
import random
from robo import Robo
from config import LARGURA, ALTURA

class RoboZigueZague(Robo):
    def __init__(self, x, y):
        super().__init__(x, y, velocidade=5)
        self.direcao = 1

    def atualizar_posicao(self):
        self.rect.y += self.velocidade
        self.rect.x += self.direcao * 3

        if self.rect.x <= 0 or self.rect.x >= LARGURA - self.rect.width:
            self.direcao *= -1

        if self.rect.y > ALTURA:
            self.kill()




