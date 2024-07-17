import pygame
from player import Player
import constants
from bullets import Bullets, Bullet
from asteroids import Asteroid, Asteroids


pygame.init()
player = Player()
constants = constants
bullets = Bullets()
bullet = Bullet(0, 0, 0)
asteroid = Asteroid()
asteroids = Asteroids()


window = pygame.display.set_mode((constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT))
running = True
pygame.display.set_caption("asteroids")

while running:
    pygame.time.delay(50)

    window.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Create a bullet using the player's current position and angle
            bullets.add_bullet(player.x, player.y, player.angle)

    keys = pygame.key.get_pressed()

    bullets.update_and_draw(window)
    player.move(window, keys)
    asteroids
    

    pygame.display.update()

pygame.quit()