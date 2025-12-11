from robo import Robo
from config import ALTURA
import pygame
import random

class RoboSaltador(Robo):
    def __init__(self, x, y):
        super().__init__(x, y, velocidade=3)

        self.salto_timer = random.randint(15, 40)
        self.dy = 2

    def atualizar_posicao(self):

        self.salto_timer -= 1
        self.rect.y += self.dy

        if self.salto_timer <= 0:
            self.dy = -5
            self.salto_timer = random.randint(15, 40)


        self.dy += 0.7

        if self.rect.y > ALTURA:
            self.kill()
