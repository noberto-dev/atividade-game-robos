from robo import Robo
from config import LARGURA, ALTURA
import pygame
class RoboCiclico(Robo):
    def __init__(self, x, y):
        super().__init__(x, y, velocidade=2)
        self.image.fill((0, 150, 255))  
        self.raio = 60
        self.centro_x = x
        self.centro_y = y

    def atualizar_posicao(self):
        self.angulo += 0.05 
        self.rect.x = self.centro_x + int(self.raio * pygame.math.cos(self.angulo))
        self.rect.y = self.centro_y + int(self.raio * pygame.math.sin(self.angulo))

        
        self.centro_y += 0.5

        if self.rect.y > ALTURA:
            self.kill()

    def update(self):
        self.atualizar_posicao()
