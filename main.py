import pygame 
import random
from entidade import Entidade
from jogador import Jogador
from robo import Robo
from tiro import Tiro
from config import LARGURA, ALTURA
from robo_ziguezague import RoboZigueZague
from robociclico import RoboCircular 
from robosaltador import RoboSaltador
from robocacador import RoboCacador
from robo_sistema import RoboLento, RoboRapido
from robochefe import Robochefe
from explosao import Explosao

if __name__ == "__main__":
    pygame.init()
    
    TELA = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Robot Defense - Template")
    Fundo = pygame.image.load('mapa1.png').convert()

    FPS = 60
    clock = pygame.time.Clock()

    chefe_robo = pygame.sprite.Group()
    tiros_robo = pygame.sprite.Group()
    todos_sprites = pygame.sprite.Group()
    inimigos = pygame.sprite.Group()
    tiros = pygame.sprite.Group()

    jogador = Jogador(LARGURA // 2, ALTURA - 60)
    todos_sprites.add(jogador)

    pontos = 0
    spawn_timer = 0

    chefe = 1
    quantidade_inimigo = 0
    quantidade_chefe = 50

    # tipos de robôs que aparecem
    tipos = [RoboLento, RoboRapido]

    rodando = True
    while rodando:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False

            # tiro
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    tiro = Tiro(jogador.rect.centerx, jogador.rect.y)
                    todos_sprites.add(tiro)
                    tiros.add(tiro)
        spawn_timer += 1        
        if len(chefe_robo) > 0 :
            if spawn_timer > 60:
               robo = RoboZigueZague(random.randint(40, LARGURA - 40), -40)
               todos_sprites.add(robo)
               inimigos.add(robo)
               spawn_timer = 0
            #timer de entrada dos inimigos
        
        elif spawn_timer > 40:
            tipo_robo = random.choice(tipos)
            robo = tipo_robo(random.randint(40, LARGURA - 40), -40)
            
            #movimento do caçador
            if isinstance(robo, RoboCacador):
                robo.set_jogador(jogador)
                
            inimigos.add(robo)
            todos_sprites.add(robo)
            spawn_timer = 0
            quantidade_inimigo +=1


            if quantidade_inimigo >= quantidade_chefe:
                robochefe = Robochefe(random.randint(40, LARGURA - 40), -40, tiros_robo, todos_sprites, jogador)
                todos_sprites.add(robochefe)
                chefe_robo.add(robochefe)


                quantidade_chefe = 50
                chefe +=1
                quantidade_chefe= quantidade_chefe * chefe
            


        # colisão tiro x robô
        colisao = pygame.sprite.groupcollide(inimigos, tiros, True, True)
        pontos += len(colisao) 
        colisaochefe = pygame.sprite.groupcollide(chefe_robo, tiros, False, True)

        for chefe,tiro_jogador in colisaochefe.items():
            for tiro in  tiro_jogador:
                chefe.vida -= 1
                pontos += 1
                explosao = Explosao(tiro.rect.centerx, tiro.rect.centery)
                todos_sprites.add(explosao)

                if chefe.vida <= 0:
                    chefe.kill()
                    pontos += 10
                    explosao_final = Explosao(chefe.rect.centerx, chefe.rect.centery)
                    todos_sprites.add(explosao_final)
                    break

        

        for robo in colisao: 
            pontos += 1
            # criar explosão no local do robô destruído
            explosao = Explosao(robo.rect.centerx, robo.rect.centery)
            todos_sprites.add(explosao)

        
        # colisão robô x jogador
        if pygame.sprite.spritecollide(jogador, inimigos, True):
            jogador.vida -= 1
            if jogador.vida <= 0:
                print("GAME OVER!")
                rodando = False
        if pygame.sprite.spritecollide(jogador, tiros_robo, True): 
            jogador.vida -= 1
            if jogador.vida <= 0:
                print("GAME OVER! Atingido por tiro do Chefe.")
                rodando = False
        

        # atualizar
        todos_sprites.update()

        # desenhar
       

        # Painel de pontos e vida
        font = pygame.font.SysFont(None, 30)
        texto = font.render(f"Vida: {jogador.vida}  |  Pontos: {pontos}", True, (255, 255, 255))
        TELA.blit(Fundo,(0, 0))
        TELA.blit(texto, (10, 10))
        todos_sprites.draw(TELA)

        pygame.display.flip()

    pygame.quit()