import pygame
import math
import constants



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.tiles = []
        self.player_pos = pygame.Vector2(constants.WINDOW_WIDTH / 2, constants.WINDOW_HEIGHT / 2)
        self.dx = 0   # direction x, like left = -1, right = 1
        self.dy = 0   # direction y, like down = 1, up = -1
        self.direction = "right"
        self.gravity = 1
        self.player_pos.x = 300
        self.player_pos.y = 300
        self.tileset_image = pygame.image.load("assets\\Characters\\Mario.png")
        self.TILE_SIZE = 32
        self.sprint_timer = 0
        self.last_key = ""
        self.y_velocity = 0
        self.x_velocity = 0
        self.velocity = 0
        self.fall_timer = 0
        self.animation_count = 0

    def get_tile(self, image, x, y, width, height):
        self.tile = pygame.Surface((width, height), pygame.SRCALPHA)
        self.tile.blit(image, (0, 0), (x * width, y * height, width, height))
        self.tile = pygame.transform.scale(self.tile, (128, 128))
        return self.tile
    
    def slice_tile(self):
        for x in range(26):  # 26 tiles in a single row
            self.tiles = self.get_tile(self.tileset_image, x, 0, constants.TILE_SIZE, constants.TILE_SIZE)  # y is 0 because all tiles are in the first row
            self.tiles.append(self.tile)
        print(self.tiles)


    def move(self, dx, dy):
        self.player_pos.x += dx
        self.player_pos.y += dy
    def move_left(self, velocity):
        self.x_velocity = -velocity
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0
    def move_right(self, velocity):
        self.x_velocity = velocity
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0
    def handle_move(self):
        keys = pygame.key.get_pressed()

        self.x_velocity = 0
        if keys[pygame.K_a]:
            self.move_left(PLAYER_VELOCITY)
        if keys[pygame.K_a]:
            self.move_right(PLAYER_VELOCITY)

    def draw(self, window, keys):
        pygame.key.set_repeat(1, 0)
        if keys[pygame.K_SPACE]:
            if self.last_key == "d":
                window.blit(self.get_tile(self.tileset_image, 13, 0, self.TILE_SIZE, self.TILE_SIZE), (self.player_pos.x, self.player_pos.y))
            elif self.last_key == "a":
                window.blit(pygame.transform.flip(self.get_tile(self.tileset_image, 13, 0, self.TILE_SIZE, self.TILE_SIZE), True, False), (self.player_pos.x, self.player_pos.y))


        elif keys[pygame.K_d]:
            self.last_key = "d"
            window.blit(self.get_tile(self.tileset_image, 9, 0, self.TILE_SIZE, self.TILE_SIZE), (self.player_pos.x, self.player_pos.y))


        elif keys[pygame.K_a]:
            self.last_key = "a"
            window.blit(pygame.transform.flip(self.get_tile(self.tileset_image, 9, 0, self.TILE_SIZE, self.TILE_SIZE), True, False), (self.player_pos.x, self.player_pos.y))

        

        if True not in keys:
            self.velocity = 0.5
            if self.last_key == "d":
                window.blit(self.get_tile(self.tileset_image, 8, 0, self.TILE_SIZE, self.TILE_SIZE), (self.player_pos.x, self.player_pos.y))
            elif self.last_key == "a":
                window.blit(pygame.transform.flip(self.get_tile(self.tileset_image, 8, 0, self.TILE_SIZE, self.TILE_SIZE), True, False), (self.player_pos.x, self.player_pos.y))
            else:
                window.blit(self.get_tile(self.tileset_image, 8, 0, self.TILE_SIZE, self.TILE_SIZE), (self.player_pos.x, self.player_pos.y))


    def update(self, window, keys, dt):
        self.draw(window, keys)
        self.move(keys, dt)