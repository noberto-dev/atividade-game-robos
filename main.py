import pygame 
import random
from entidade import Entidade
from jogador import Jogador
from robo import Robo
from tiro import Tiro
from config import LARGURA, ALTURA
from robo_ziguezague import RoboZigueZague
from robociclico import RoboCiclico 
from robosaltador import RoboSaltador

if __name__ == "__main__":
    pygame.init()
    
    TELA = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Robot Defense - Template")

    FPS = 60
    clock = pygame.time.Clock()

    todos_sprites = pygame.sprite.Group()
    inimigos = pygame.sprite.Group()
    tiros = pygame.sprite.Group()

    jogador = Jogador(LARGURA // 2, ALTURA - 60)
    todos_sprites.add(jogador)

    pontos = 0
    spawn_timer = 0
    tipos = [RoboZigueZague, RoboCiclico, RoboSaltador]
    rodando = True
    while rodando:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    tiro = Tiro(jogador.rect.centerx, jogador.rect.y)
                    todos_sprites.add(tiro)
                    tiros.add(tiro)
                    todos_sprites.add(robo)
            

        # timer de entrada dos inimigos

        
        spawn_timer += 1
        if spawn_timer > 40:
            tipo_robo = random.choice(tipos)
            robo = tipo_robo((random.randint(40, LARGURA - 40), -40))
            inimigos.add(robo)
            spawn_timer = 0
        # colisão tiro x robô
        colisao = pygame.sprite.groupcollide(inimigos, tiros, True, True)
        pontos += len(colisao)

        # colisão robô x jogador
        if pygame.sprite.spritecollide(jogador, inimigos, True):
            jogador.vida -= 1
            if jogador.vida <= 0:
                print("GAME OVER!")
                rodando = False

        # atualizar
        todos_sprites.update()

        # desenhar
        TELA.fill((20, 20, 20))
        todos_sprites.draw(TELA)

        #Painel de pontos e vida
        font = pygame.font.SysFont(None, 30)
        texto = font.render(f"Vida: {jogador.vida}  |  Pontos: {pontos}", True, (255, 255, 255))
        TELA.blit(texto, (10, 10))

        pygame.display.flip()

    pygame.quit()
