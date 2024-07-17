import pygame
import math
import constants
import player

pygame.init()

Player = player.Player()
window = pygame.display.set_mode((constants.WINDOW_WIDTH,constants.WINDOW_HEIGHT))
clock = pygame.time.Clock()
Player_group = pygame.sprite.GroupSingle(player.Player())
sprite_group = pygame.sprite.Group()
running = True
dt = 0
tile_x = 0
tile_y = 0

class Tile:
    def __init__(self):
        self.x = 50
        self.y = 50
        self.color = ()
        self.number = 0
        self.size_x = 100
        self.size_y = 100
        self.x_list_area = []
        self.y_list_area = []

tile = Tile()



while running:
    dt = clock.tick(60)  # Get the time passed since last tick, limit to 60 FPS
    keys = pygame.key.get_pressed()

        # Render the tiles
    for i, tile in enumerate(Player.tiles):
        tile_x = (i % 13) * constants.TILE_SIZE  # Calculate x position for the tile
        tile_y = (i // 13) * constants.TILE_SIZE  # Calculate y position for the tile
        window.blit(tile, (tile_x, tile_y))  # Draw the tile on the screen

    window.fill((92, 148, 252))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    rect = pygame.Rect(50, 50, 100, 100)
    rect1 = pygame.draw.rect(window, (0, 40, 0), rect)
    

    Player.update(window, keys, dt)

    pygame.display.flip()
    dt = clock.tick(60) / 1000


pygame.quit()