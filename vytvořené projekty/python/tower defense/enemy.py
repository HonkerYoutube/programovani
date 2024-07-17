import pygame as pg
import random

class Enemy(pg.sprite.Sprite):
    def __init__(self, waypoints, image):
        pg.sprite.Sprite.__init__(self)
        self.waypoints = waypoints
        self.pos = pg.Vector2(waypoints[0])
        self.next = 1
        self.image = pg.image.load("assets\\images\\enemies\\enemy_1.png")
        self.image = image
        self.rect = self.image.get_rect()   #getting his hitbox
        self.rect.center = self.pos
        self.speed = random.randint(2, 10)
        self.score = 0

    def move(self):
        self.target = pg.Vector2(self.waypoints[self.next])
        self.movement = self.target - self.pos
        dist = self.movement.length()   #distance
        if self.waypoints[self.next - 1] == self.waypoints[-1]:
            self.kill()
        if dist < self.speed:
            if dist != 0:
                self.pos += self.movement.normalize() * dist
            if self.next < len(self.waypoints) - 1:
                self.next += 1
        else:
            self.pos += self.movement.normalize() * self.speed
        
        self.rect.center = self.pos


    def update(self):
        self.move()


    def kill(self):
        score += 1
        pg.sprite.Sprite.kill(self)



class WeakEnemy(Enemy):
    def __init__(self, pos):
        super().__init__(pos)
        self.health = 1
        self.image = pg.image.load("tower defense\\assets\\images\\enemies\\enemy_1.png")


    def move(self):
        self.rect.x += 2

class MediumEnemy(Enemy):
    def __init__(self, pos):
        super().__init__(pos)
        self.health = 5
        self.image = pg.image.load("tower defense\\assets\\images\\enemies\\enemy_2.png")

        
    def move(self):
        self.rect.x += 0.5

    


class StrongEnemy(Enemy):
    pass