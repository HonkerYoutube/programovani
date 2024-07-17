#!!!!!!!!!!!!!!!!!! na všechno používej funkce !!!!!!!!!!!!!!!!!!!
import pygame
import sys
import random

pygame.font.init()
font = pygame.font.Font(None, 50)
text_surface = font.render('you died', True, (0, 0, 0))
window_width = 1200
window_height = 800
window = pygame.display.set_mode((window_width, window_height))
running = True
title = pygame.display.set_caption("flappy bird")
FPS = 60
clock = pygame.time.Clock()
dt = 0
gravity = 0.98
end = False

def end_the_game():
    window.blit(text_surface, (window_width / 2 - text_surface.get_width(), window_height / 2))
    end = True
    running = False

class Bird:
    def __init__(self):
        self.velocity = 0
        self.gravity = 0.5
        self.jump_strength = -10

        self.x = 50
        self.y = 300
        self.image = pygame.image.load("flappy bird\\assets\\flappy-bird-transparent-background.png").convert()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    def update(self, keys):
        self.calculate()
        self.move(keys)
        window.blit(self.image, (self.x, self.y))
    def calculate(self):
        self.velocity += self.gravity
        self.y += self.velocity
    def jump(self):
        self.velocity = self.jump_strength



    def move(self, keys):
        if keys[pygame.K_SPACE]:
            self.jump()




class Pipe:
    def __init__(self):
        self.image = pygame.image.load("flappy bird\\assets\\pipe.png").convert()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = 850
        self.y = random.randint(-645, -147)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    def update(self):
        window.blit(self.image, (self.x, self.y))

pipe = Pipe()
bird = Bird()
pipes = []

while running:
    keys = pygame.key.get_pressed()
    window.fill((255, 255, 255))
    clock.tick(FPS)
    pipe.update()
    bird.update(keys)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
    if bird.y > 850 or bird.y < -50:
        end_the_game()






    dt = clock.tick(FPS)/1000
    pygame.display.flip()