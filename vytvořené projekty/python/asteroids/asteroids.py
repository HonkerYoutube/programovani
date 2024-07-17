import pygame
import random
import constants


class Asteroid:
    def __init__(self, ):
        self.x = 0
        self.y = 0
        self.direction = 0
        self.size = 2   # 1 small  2 medium  3 big
        self.speed = 0
        self.is_active = True
        self.num = 0

    class Small:
        def __init__(self):
            self.radius = 10
            self.health = 10
        
    class Medium:
        def __init__(self):
            self.radius = 20
            self.health = 15

    class Big:
        def __init__(self):
            self.radius = 30
            self.health = 20

    def update(self):
        if self.speed < 1:
            self.is_active = False
            self.num = random.randint(1, 4)

        
    def draw(self, win):
        if self.is_active == True:
            if self.num == 1 or self.num == 2:
                pygame.draw.circle(win, constants.BLUE, (self.x, self.y), small.radius)
            if self.num == 3:
                pygame.draw.circle(win, constants.BLUE, (self.x, self.y), small.radius)
            if self.num == 4:
                pygame.draw.circle(win, constants.BLUE, (self.x, self.y), small.radius)



class Asteroids:
    def __init__(self):
        self.asteroids = []

    def add_asteroid(self, x, y, angle, speed):
        self.asteroids.append(Asteroid())

    def update_and_draw(self, win):
        for asteroid in self.asteroids:
            asteroid.update()
            asteroid.draw(win)
        self.asteroids = [asteroid for asteroid in self.asteroids if asteroid.is_active]

small = Asteroid.Small()