import pygame
import constants

class Player2(pygame.sprite.Sprite):
    def __init__(self, group):
        pygame.sprite.Sprite.__init__(self, group) 
        self.name = "player2"
        self.image = pygame.image.load("assets\\arts\\Player2.png")
        self.mask = pygame.mask.from_surface(self.image)
        self.x = constants.WINDOW_WIDTH - self.image.get_width()
        self.y = constants.WINDOW_HEIGHT / 2
        self.size_x = self.image.get_width()
        self.size_y = self.image.get_height()
        self.surface_x = self.x + self.size_x
        self.surface_y = self.y + self.size_y
        self.width = 20
        self.height = 80
        self.gameStarted = False
        self.score = 0
        

    def move(self, keys, dt):
        if self.y < 48:
            self.y = 48
        if self.y + self.size_y > constants.WINDOW_HEIGHT:
            self.y = constants.WINDOW_HEIGHT - self.size_y

        if keys[pygame.K_UP]:
            self.y -= 150 * dt
            self.gameStarted = True
        
        elif keys[pygame.K_DOWN]:
            self.y += 150 * dt
            self.gameStarted = True
        
    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

    def update(self, keys, dt, window):
        self.move(keys, dt)
        self.draw(window)