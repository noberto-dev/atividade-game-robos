import pygame

class Explosao(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.frames = []
        for i in range(11):
            img = pygame.image.load(f"explosao_sprites\explosion-d{i}.png").convert_alpha()
            self.frames.append(img)

        self.frame_atual = 0
        self.image = self.frames[self.frame_atual]
        self.rect = self.image.get_rect(center=(x, y))

        self.tempo_frame = 50  
        self.ultimo_update = pygame.time.get_ticks()

    def update(self):
        agora = pygame.time.get_ticks()
        if agora - self.ultimo_update > self.tempo_frame:
            self.ultimo_update = agora
            self.frame_atual += 1

            if self.frame_atual >= len(self.frames):
                self.kill()
            else:
                self.image = self.frames[self.frame_atual]
