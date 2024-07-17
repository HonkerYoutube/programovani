import math
import pygame
import constants

class Bullet:
    def __init__(self, x, y, angle, speed=30, width=10, height=10):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = speed
        self.width = width
        self.height = height
        self.is_active = True
        self.vertices = []
        self.calculate_vertices()

    def calculate_vertices(self):
        base = self.width
        height = self.height
        self.vertices = [
            (self.x - base / 2, self.y + height / 2),
            (self.x + base / 2, self.y + height / 2),
            (self.x + base / 2, self.y - height / 2),
            (self.x - base / 2, self.y - height / 2),
        ]

    def update(self):
        self.x += self.speed * math.cos(self.angle - math.pi / 2)
        self.y += self.speed * math.sin(self.angle - math.pi / 2)
        self.speed *= 0.98  # Slow down over time
        if self.speed < 1:
            self.is_active = False
        self.calculate_vertices()

    def draw(self, win):
        if self.is_active:
            min_x = min(self.vertices, key=lambda t: t[0])[0]
            max_x = max(self.vertices, key=lambda t: t[0])[0]
            min_y = min(self.vertices, key=lambda t: t[1])[1]
            max_y = max(self.vertices, key=lambda t: t[1])[1]
            bounding_rect = (int(min_x), int(min_y), int(max_x - min_x), int(max_y - min_y))
            pygame.draw.rect(win, constants.RED, bounding_rect)


class Bullets:
    def __init__(self):
        self.bullets = []

    def add_bullet(self, x, y, angle):
        self.bullets.append(Bullet(x, y, angle))

    def update_and_draw(self, win):
        for bullet in self.bullets:
            bullet.update()
            bullet.draw(win)
        self.bullets = [bullet for bullet in self.bullets if bullet.is_active]