import pygame as pg
from constant import *
from enemy import Enemy
from world import World
import json
import random

pg.init()

clock = pg.time.Clock()

screen = pg.display.set_mode((SIZE_WIDTH, SIZE_LENGTH))


map_image = pg.image.load("assets\\levels\\level.png")
with open("assets\\levels\\level.tmj") as file:
    data = json.load(file)
world = World(data, map_image)
world.process_data()

enemy_class = Enemy([], 0)
pg.display.set_caption(f"tower defense   score: {enemy_class.score}")

enemy_image1 = pg.image.load("assets\\images\\enemies\\enemy_1.png")
enemy_image2 = pg.image.load("assets\\images\\enemies\\enemy_2.png")
enemy_image3 = pg.image.load("assets\\images\\enemies\\enemy_3.png")
enemy_image4 = pg.image.load("assets\\images\\enemies\\enemy_4.png")


enemy_group = pg.sprite.Group()


def spawn():
    enemy = Enemy(world.waypoints, random.choice([enemy_image1, enemy_image2, enemy_image3, enemy_image4]))
    enemy_group.add(enemy)
    
SPAWN = pg.USEREVENT
pg.time.set_timer(SPAWN, random.randint(500, 5000))

running = True

while running:
    clock.tick(FPS)

    screen.fill(0)

    world.draw(screen)

    enemy_group.update()
    enemy_group.draw(screen)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == SPAWN:
            spawn()
        elif event.type == pg.MOUSEBUTTONDOWN:
            for enemy in enemy_group:
                if enemy.rect.collidepoint(event.pos):
                    if random.choice([True, False]):
                        enemy.kill()


    pg.display.flip()


pg.quit()
