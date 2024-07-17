import pygame

pygame.init()

running = True
window = pygame.display.set_mode((300, 400))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    window.fill((0, 0, 0))   #white



    
    pygame.display.flip()
    