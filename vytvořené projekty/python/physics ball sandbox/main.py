import pygame
import pymunk

pygame.init()
FPS = 60
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 700
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = True
group = pygame.sprite.Group()
mouse_pos = pygame.mouse.get_pos()
clock = pygame.time.Clock()
gravity = 10
pymunk.Body

BOX_WIDTH = WINDOW_WIDTH
BOX_HEIGHT = WINDOW_HEIGHT
BOX_X = (WINDOW_WIDTH - BOX_WIDTH) // 2
BOX_Y = (WINDOW_HEIGHT - BOX_HEIGHT) // 2
BOX_COLOR = (0, 255, 0)



class Ball(pymunk.Body):
    def __init__(self):
        self.spawned = False
        self.x = 350
        self.y = 350
        self.RADIUS = 20
        self.vx = 350
        self.vy = 350
        self.ax = 0   # acceleration x
        self.ay = 0   # acceleration y
        self.color = (255, 0, 0)
        self.elasticity = 1

    def draw(self):
        if self.spawned == False:
            self.x = mouse_pos[0]
            self.y = mouse_pos[1]
        pygame.draw.circle(window, self.color, (self.x, self.y), self.RADIUS)
    def calculations(self, dt):
        if self.spawned == True:
            self.vy += self.ay
            self.vy += self.ay

            self.x = self.vx
            self.y = self.vy

            self.ay += gravity * dt
        else:
            self.vx = mouse_pos[0]
            self.vy = mouse_pos[1]

    def update(self, dt):
        self.calculations(dt)
        self.draw()



ball = Ball()


while running:

    dt = clock.tick(FPS) / 1000.0
    mouse_pos = pygame.mouse.get_pos()
    window.fill((255, 255, 255))
    ball.update(dt)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            ball.spawned = True


    if ball.x - ball.RADIUS < BOX_X or ball.x + ball.RADIUS > BOX_X + BOX_WIDTH:
        ball.vx = -(ball.vx - ball.elasticity)  # Reverse horizontal velocity
    if ball.y - ball.RADIUS < BOX_Y or ball.y + ball.RADIUS > BOX_Y + BOX_HEIGHT:
        ball.vy = -(ball.vy - ball.elasticity)  # Reverse vertical velocity
    print(ball.ay)
    # pygame.draw.rect(window, BOX_COLOR, (BOX_X, BOX_Y, BOX_WIDTH, BOX_HEIGHT))






    pygame.display.flip()