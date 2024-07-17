import pygame
import time

window_width, window_height = 600, 600
window = pygame.display.set_mode((window_width, window_height))
running = True
mouse = pygame.mouse

class StartBlock:
    def __init__(self):
        self.x = window_width / 2
        self.y = window_height / 2
        self.placed = False
        self.color = (0, 0, 255)
        self.rect = pygame.Rect(self.x, self.y, block.size, block.size)

    def update(self):
        self.draw()

    def draw(self):
        pygame.draw.rect(window, self.color, self.rect)


class Block:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 50
        self.expand_x1, self.expand_x2 = self.x + self.size, self.x - self.size
        self.expand_y1, self.expand_y2 = self.y + self.size, self.y - self.size
        self.is_colored = False
        self.color = (0, 0, 255)

    def expand(self):
        for x in blocks.taken_blocks_x:
            for y in blocks.taken_blocks_y:
                if x != self.expand_x1:
                    pygame.draw.rect(window, self.color, (self.expand_x1, y, self.size, self.size))
                elif x != self.expand_x2:
                    pygame.draw.rect(window, self.color, (self.expand_x2, y, self.size, self.size))
                
                if y != self.expand_y1:
                    pygame.draw.rect(window, self.color, (self.x, self.expand_y1, self.size, self.size))
                elif y != self.expand_y2:
                    pygame.draw.rect(window, self.color, (self.x, self.expand_y2, self.size, self.size))

    def draw(self):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.size, self.size))
    def update(self):
        self.draw()
        self.expand()


    

class Blocks:
    def __init__(self):
        self.blocks = []
        self.taken_blocks_x = []
        self.taken_blocks_y = []
    def draw_grid(self):
        for x1 in range(0, window_width, block.size):
            for y1 in range(0, window_height, block.size):
                # self.blocks.append(Block(x1, y1))
                pygame.draw.rect(window, (0, 0, 0), (x1, y1, x1 + block.size, y1 + block.size), 1)


blocks = Blocks()
block = Block()
startblock = StartBlock()




while running:
    startblock.update()
    window.fill((255, 255, 255))
    blocks.draw_grid()
    pygame.time.wait(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            startblock.placed = True




    pygame.display.flip()