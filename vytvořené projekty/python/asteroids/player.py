import math
import pygame
import constants

constants = constants
mouse = pygame.mouse


class Player:
    def __init__(self):
        self.x = 200
        self.y = 200
        self.vel_x = 0
        self.vel_y = 0
        self.acceleration = 1
        self.friction = 0.05
        self.max_speed = 15
        self.angle = 0

    def move(self, win, keys):
        # Define the vertices of the isosceles triangle
        height = 23
        base = 30
        vertices = [(0, -height), (-base / 2, height / 2), (base / 2, height / 2)]
        

        # Get mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Calculate the angle between the player and the mouse position
        self.angle = math.atan2(mouse_y - self.y, mouse_x - self.x)
        self.angle += math.pi / 2

        # Rotate vertices based on the calculated angle
        rotated_vertices = []
        for vx, vy in vertices:
            rotated_x = vx * math.cos(self.angle) - vy * math.sin(self.angle)
            rotated_y = vx * math.sin(self.angle) + vy * math.cos(self.angle)
            rotated_vertices.append((self.x + rotated_x, self.y + rotated_y))

        # Draw the rotated polygon
        pygame.draw.polygon(win, constants.BLACK, rotated_vertices)

        # Horizontal Movement
        if keys[pygame.K_a]:
            self.vel_x -= self.acceleration
        elif keys[pygame.K_d]:
            self.vel_x += self.acceleration
        else:
            self.vel_x *= (1 - self.friction)  # Apply friction

        # Vertical Movement
        if keys[pygame.K_w]:
            self.vel_y -= self.acceleration
        elif keys[pygame.K_s]:
            self.vel_y += self.acceleration
        else:
            self.vel_y *= (1 - self.friction)  # Apply friction

        # Cap the speed
        speed = math.sqrt(self.vel_x ** 2 + self.vel_y ** 2)
        if speed > self.max_speed:
            scale = self.max_speed / speed
            self.vel_x *= scale
            self.vel_y *= scale

        # Update the player's position
        self.x += self.vel_x
        self.y += self.vel_y

        # Screen wrapping logic
        if self.x < 0:
            self.x = constants.WINDOW_WIDTH
        elif self.x > constants.WINDOW_WIDTH:
            self.x = 0
        if self.y < 0:
            self.y = constants.WINDOW_HEIGHT
        elif self.y > constants.WINDOW_HEIGHT:
            self.y = 0

        # Draw the final polygon with the updated position
        rotated_vertices = []
        for vx, vy in vertices:
            rotated_x = vx * math.cos(self.angle) - vy * math.sin(self.angle)
            rotated_y = vx * math.sin(self.angle) + vy * math.cos(self.angle)
            rotated_vertices.append((self.x + rotated_x, self.y + rotated_y))

        pygame.draw.polygon(win, constants.WHITE, rotated_vertices)
