import pygame
import math
from entidade import Entidade
from config import *


class Tirorobo(Entidade):
    def __init__(self, x, y, jogador_x, jogador_y):
        super().__init__(x, y, velocidade = 7)
        self.image.fill((255,255,255))

        dx = jogador_x - self.rect.centerx
        dy = jogador_y - self.rect.centery

        distancia = math.hypot(dx, dy)



        if distancia >0:
            self.dx = dx / distancia
            self.dy = dy /distancia
        else:
            self.dx = 0
            self.dy=1
            

    def update(self):
        self.rect.x += self.dx *self.velocidade
        self.rect.y += self.dy * self.velocidade
        if (self.rect.y > ALTURA or self.rect.y < 0 or self.rect.x > LARGURA or self.rect.x < 0):
            self.kill()