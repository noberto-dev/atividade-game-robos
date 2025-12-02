from robo import Robo
from config import LARGURA, ALTURA
import pygame
import math

class RoboCircular(Robo):
    def __init__(self, x, y, raio=60, velocidade_rotacao=0.25):
        super().__init__(x, y, velocidade=5)
        self.raio = raio
        self.velocidade_rotacao = velocidade_rotacao
        self.angulo = 0 
        self.centro = pygame.Vector2(x, y)
        self.image.fill((0, 100, 255))

    def atualizar_posicao(self):
        self.angulo += self.velocidade_rotacao
        self.rect.x = self.centro.x + math.cos(self.angulo) * self.raio
        self.rect.y = self.centro.y + math.sin(self.angulo) * self.raio
        self.centro.y += self.velocidade

    def update(self,):
     self.atualizar_posicao()