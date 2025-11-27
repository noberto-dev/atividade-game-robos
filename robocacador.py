from robo import Robo
from config import LARGURA, ALTURA


class RoboCacador(Robo):
    def __init__(self, x, y, jogador):
        super().__init__(x, y, velocidade=2.2)
        self.image.fill((200, 0, 200))  
        self.jogador = jogador

    def atualizar_posicao(self):
    
        dx = self.jogador.rect.centerx - self.rect.centerx
        dy = self.jogador.rect.centery - self.rect.centery

       
        dist = max(1, abs(dx) + abs(dy))
        self.rect.x += int(self.velocidade * (dx / dist) * 3)
        self.rect.y += int(self.velocidade * (dy / dist) * 3)

        if self.rect.y > ALTURA:
            self.kill()

    def update(self):
        self.atualizar_posicao()