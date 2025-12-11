import pygame
from entidade import *
from config import *


class Robo(Entidade):
    def __init__(self, x, y, velocidade):
        super().__init__(x, y, velocidade)

        self.sprites = [pygame.image.load("assets/boss/almo1.png"),
                        pygame.image.load("assets/boss/almo2.png"),
                        pygame.image.load("assets/boss/almo3.png"),
                        pygame.image.load("assets/boss/almo4.png"),
                        pygame.image.load("assets/boss/almo5.png"),]  

        # CONTROLE DE ANIMAÇÃO
        self.frame = 0
        self.velocidade_animacao = 0.15


        self.image = pygame.Surface((40, 40))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(x, y))


    def animar(self):
        if not self.sprites:
            return

        self.frame += self.velocidade_animacao
        if self.frame >= len(self.sprites):
            self.frame = 0

        self.image = self.sprites[int(self.frame)]
        old_center = self.rect.center
        self.rect = self.image.get_rect(center=old_center)


    def update(self):
        self.animar()
        self.atualizar_posicao()

    def atualizar_posicao(self):
        raise NotImplementedError

