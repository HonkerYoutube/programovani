import pygame
import constants
import player1
import player2
import ball


pygame.font.init()
font = pygame.font.Font("assets\\fonts\\Teko\\Teko-VariableFont_wght.ttf", 32)
group = pygame.sprite.Group()
Player1 = player1.Player1(group)
Player2 = player2.Player2(group)
Ball = ball.Ball(group)


group.add(Player1)
group.add(Player2)
group.add(Ball)


window = pygame.display.set_mode((constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT))
running = True
keys = pygame.key.get_pressed()
clock = pygame.time.Clock()




class Background:
    def __init__(self):
        self.image = pygame.image.load("assets\\arts\\Board.png")
        self.size_x = self.image.get_width()
        self.size_y = self.image.get_height()
        self.x = 0
        self.y = constants.WINDOW_HEIGHT - self.size_y



background = Background()




class Background_of_score:
    def __init__(self):
        self.image = pygame.image.load("assets\\arts\\ScoreBar.png")
        self.size_x = self.image.get_width()
        self.size_y = self.image.get_height()
        self.x = 0
        self.y = 0
        self.y /= 2



class Score_text():
    def __init__(self, player):
        self.text = font.render(str(player.score), True, (0, 0, 0))
        print(f"{player.name}: {player.score}")
        self.rect = self.text.get_rect()
        self.x = 100
        self.y = background_of_score.y // 2



background_of_score = Background_of_score()
background_of_score1 = Background_of_score()
background_of_score2 = Background_of_score()
background_of_score2.x += constants.WINDOW_WIDTH - background_of_score2.size_y - 293
background_of_score2.image = pygame.transform.flip(background_of_score2.image, True, False)
score_text1 = Score_text(Player1)
score_text2 = Score_text(Player2)
score_text2.x = background_of_score2.x





while running:
    window.blit(score_text1.text, score_text1.rect)
    window.blit(score_text2.text, score_text2.rect)
    window.blit(background.image, (background.x, background.y))
    window.blit(background_of_score1.image, (background_of_score1.x, background_of_score1.y))
    window.blit(background_of_score2.image, (background_of_score2.x, background_of_score2.y))
    keys = pygame.key.get_pressed()
    dt = clock.tick(constants.FPS)/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.K_SPACE:
            gameStarted = True

    Player1.update(keys, dt, window, background)
    Player2.update(keys, dt, window)
    if Player1.gameStarted == True or Player2.gameStarted == True:
        Ball.calculate(dt)

    Ball.draw(window)

    
    


        
    pygame.display.flip()