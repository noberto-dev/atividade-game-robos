import pygame
from entidade import *
from config import *


# ROBO BASE
class Robo(Entidade):
    def __init__(self, x, y, velocidade):
        super().__init__(x, y, velocidade)
        self.image.fill((255, 0, 0)) 
    def atualizar_posicao(self):
        raise NotImplementedError

