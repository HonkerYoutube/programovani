import pygame
from food import Food


food = Food()


class Player:
    def __init__(self):
        self.x = 400
        self.y = 400

        self.width = 50
        self.height = 50
        self.score = 0
        self.direction = (0, 0) 
        self.mowing = False
        self.parts = []
        self.parts_x = []
        self.parts_y = []

    
    def move(self, win, keys, food):
        pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, self.width, self.height))
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction = (-1, 0)
            self.mowing = True
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction = (1, 0)
            self.mowing = True
        
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direction = (0, -1)
            self.mowing = True
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction = (0, 1)
            self.mowing = True

        if self.mowing:
            self.x += self.direction[0] * 50
            self.y += self.direction[1] * 50

        
        if self.x < 0:
            self.x = 750
            # pygame.quit()
        if self.x > 750:
            self.x = 0
            # pygame.quit()
        
        if self.y < 0:
            self.y = 750
            # pygame.quit()
        if self.y > 750:
            self.y = 0
            # pygame.quit()

        self.eat(food)

        pygame.draw.rect(win, (0, 255, 0), (self.x, self.y, self.width, self.height))

    
    def move_parts(self, win, i1):
        math1 = 0
        if self.direction[0] == -1:   # x
            math1 = self.direction[0] - 50
            self.parts_x.append(self.x + math1)

        # elif self.direction[1] != 0:   #y
        #     print(f"self.y: {self.y}")
        #     math1 = self.direction[1] * 50
        #     self.parts_y.append(self.y)
            


        # print(f"self.x: {self.x}   self.direction_x: {self.direction[0]}   self.direction_y: {self.direction[1]}")


        pygame.draw.rect(win, (0, 0, 0), (self.parts_x[0], self.parts_y[0], self.width, self.height))
        pygame.draw.rect(win, (0, 255, 0), (self.parts_x[0], self.parts_y[0], self.width, self.height))
        

# ctrl k ctrl c   přidá #
# ctrl k ctrl u   odstraní #
# ctrl d   označí stejné věci

    def eat(self, food):
        if self.x == food.x and self.y == food.y:
            food.ate = True
            self.score += 1
            self.parts.append(self.score)