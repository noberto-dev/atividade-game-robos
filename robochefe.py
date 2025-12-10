import pygame
from config import *
from tiro_robo import Tirorobo
from robo import Robo


class Robochefe(Robo):
    def __init__(self, x, y, tiros_robo, todos_sprites, jogador_referencia):
        super().__init__(x, y, velocidade=1.5)

        self.sprites = [
            pygame.image.load("mov1.png").convert_alpha(),
            pygame.image.load("mov2.png").convert_alpha(),
            pygame.image.load("mov3.png").convert_alpha(),
            pygame.image.load("mov4.png").convert_alpha(),
            pygame.image.load("mov5.png").convert_alpha(),
            pygame.image.load("mov6.png").convert_alpha(),
        ]

        self.frame = 0
        self.velocidade_animacao = 0.15  
        self.image = self.sprites[0]
        self.rect = self.image.get_rect(center=(x, y))

        self.direcao = 1
        self.intervalo = 600
        self.ultimo_tiro = 0
        self.vida = 10

        self.tiros_robo = tiros_robo
        self.todos_sprites = todos_sprites
        self.jogador = jogador_referencia

    def animar(self):
        self.frame += self.velocidade_animacao
        if self.frame >= len(self.sprites):
            self.frame = 0

        self.image = self.sprites[int(self.frame)]

    def atualizar_posicao(self):
        if self.rect.y < 50: 
            self.rect.y += self.velocidade

        self.rect.x += self.direcao * 3

        if self.rect.x <= 0 or self.rect.x >= LARGURA - self.rect.width:
            self.direcao *= -1


    def update(self):
        self.animar()              
        self.atualizar_posicao()   
        

        if self.vida <= 0:
            self.kill()

        tempo_atual = pygame.time.get_ticks()
        if tempo_atual > self.ultimo_tiro + self.intervalo:
            self.disparo()
            self.ultimo_tiro = tempo_atual

    def disparo(self):
        jogador_x = self.jogador.rect.centerx
        jogador_y = self.jogador.rect.centery

        novo_tiro = Tirorobo(self.rect.centerx, self.rect.bottom, jogador_x, jogador_y)
        self.tiros_robo.add(novo_tiro)
        self.todos_sprites.add(novo_tiro)
