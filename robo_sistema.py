import pygame
from robo_ziguezague import RoboZigueZague
from config import LARGURA

class RoboLento(RoboZigueZague):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image.fill((190, 145, 205))
        self.velocidade = 1
    def atualizar_posicao(self):
        self.rect.y += self.velocidade
        self.rect.x += self.direcao * 1
        if self.rect.x <= 0 or self.rect.x >= LARGURA - 40:
            self.direcao *= -1

    

class RoboRapido(RoboZigueZague):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image.fill((125, 178, 200))
        self.velocidade = 5
        
    def atualizar_posicao(self):
        self.rect.y += self.velocidade
        self.rect.x += self.direcao * 8

        if self.rect.x <= 0 or self.rect.x >= LARGURA - 40:
            self.direcao *= -1


