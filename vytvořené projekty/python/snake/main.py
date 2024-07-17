import pygame
from player import Player
from food import Food

pygame.init()

window = pygame.display.set_mode((800,800))
running = True
display = pygame.display


player = Player()
food = Food()

def grid():
    for i in range(0, 800, 50):
        for y in range(0, 800, 50):
            rect = pygame.Rect(i, y, i + 50, y + 50)
            pygame.draw.rect(window, (0, 77, 0), rect, 1)



while running:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    grid()

    
    pygame.display.set_caption(f"snake   score: {player.score}")

    for i1 in range(player.score):
        player.move_parts(window, i1)
    
    

    keys = pygame.key.get_pressed()
    player.parts_x.append(player.x)
    player.parts_y.append(player.y)
    player.move(window, keys, food)
    food.spawn(window)

    display.flip()