import pygame
import random



class Food:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 50
        self.height = 50
        self.ate = True


    def spawn(self, win):
        if self.ate:
            self.x = int(random.randint(0,750) / 50) * 50
            self.y = int(random.randint(0,750) / 50) * 50
            pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.width, self.height))
            self.ate = False
