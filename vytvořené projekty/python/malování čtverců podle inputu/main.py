import pygame

window = pygame.display.set_mode((600, 600))
running = True
x = []
y = []

RECT_COLOR = 0, 0, 0


x = input("rectangle coordinate x (2, from left to right):   ")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    pygame.display.flip()
