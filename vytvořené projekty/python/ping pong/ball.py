import pygame
import constants
import random
import math
import player1
import player2

background = pygame.image.load("assets\\arts\\Board.png")

class Ball(pygame.sprite.Sprite):
    def __init__(self, group):
        pygame.sprite.Sprite.__init__(self, group) 
        self.image = pygame.image.load("assets\\arts\\Ball.png")
        self.mask = pygame.mask.from_surface(self.image)
        self.x = constants.WINDOW_WIDTH / 2 + self.image.get_width() - 45
        self.y = constants.WINDOW_HEIGHT - background.get_height() + background.get_height() / 2 - 45
        print(self.x, self.y)
        self.radius = self.image.get_width()
        self.speed = 150
        # self.vx = random.randint(-10, 10)   #velocity x
        # self.vy = random.randint(-10, 10)   #velocity y
        # while self.vx + self.vy != self.speed:
        #     self.vx = random.randint(-10, 10)   #velocity x
        #     self.vy = random.randint(-10, 10)   #velocity y
        self.vy = 150
        self.vx = 0
        self.direction = math.sin(self.vx + self.vy)


        self.Player1 = player1.Player1(group)
        self.Player2 = player2.Player2(group)



    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
    def calculate(self, dt):
        if self.x - self.radius == self.Player1.x - self.Player1.width:
            self.Player1.score += 1
            print(f"Player1: {self.Player1.score}, Player2: {self.Player2.score}")
            self.vy *= -1

        if self.x + self.radius == self.Player2.x - self.Player2.width:
            self.Player2.score += 1
            print(f"Player1: {self.Player1.score}, Player2: {self.Player2.score}")
            self.vy *= -1

        if self.y - 10 < 145 or self.y + 20 > constants.WINDOW_HEIGHT:
            self.vy *= -1
        
        self.x += self.vx * dt
        self.y += self.vy * dt
