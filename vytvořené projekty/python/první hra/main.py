import pygame

width, height = 900, 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("space ships")

def main():
    
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()