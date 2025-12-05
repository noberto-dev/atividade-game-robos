import pygame
from config import *
from tiro_robo import Tirorobo
from robo import Robo


class Robochefe(Robo):
    def __init__(self, x, y, tiros_robo, todos_sprites, jogador_referencia):
        super().__init__(x, y, velocidade =4)
        self.direcao = 1
        self.image.fill((55, 255, 0))
        self.intevalo = 400
        self.ultimo_tiro = 0


        self.tiros_robo = tiros_robo
        self.todos_sprites = todos_sprites
        self.jogador = jogador_referencia

    def atualizar_posicao(self):
        if self.rect.y < 50: 
            self.rect.y += self.velocidade
        self.rect.x += self.direcao * 3

        if self.rect.x <= 0 or self.rect.x >= LARGURA - 40:
            self.direcao *= -1

    def update(self):
        
        self.atualizar_posicao()
        if self.rect.y > ALTURA:
            self.kill()

        tempo_atual = pygame.time.get_ticks()

        if tempo_atual > self.ultimo_tiro + self.intevalo:

            self.disparo()

            self.ultimo_tiro = tempo_atual

    def disparo(self):

        jogador_x = self.jogador.rect.centerx
        jogador_y = self.jogador.rect.centery

        novo_tiro = Tirorobo(self.rect.centerx, self.rect.bottom, jogador_x,jogador_y)
        self.tiros_robo.add(novo_tiro)
        self.todos_sprites.add(novo_tiro)