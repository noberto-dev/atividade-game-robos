import pygame
from robo import Robo

class RoboCacador(Robo):
    def __init__(self, x, y):
        super().__init__(x, y, velocidade=7)

        from jogador import Jogador
        self.jogador = None 
        self.image.fill((255, 0, 255))

    def set_jogador(self, jogador):
        self.jogador = jogador

    def update(self):
        if self.jogador is None:
            return
        
        dx = self.jogador.rect.centerx - self.rect.centerx
        dy = self.jogador.rect.centery - self.rect.centery

        dist = (dx*dx + dy*dy)**0.5
        if dist > 0:
            dx /= dist
            dy /= dist

        self.rect.x += dx * self.velocidade
        self.rect.y += dy * self.velocidade
