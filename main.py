import time
import pygame
from sys import exit
import random
def showscore(score):
    font = pygame.font.Font(None, 25)
    Score = font.render(f"Your score: {score}",False,"Blue")
    score_rect = Score.get_rect(topleft = (0,0))
    screen.blit(Score,score_rect)

pygame.init()

#Important variables
dis_width = 720
dis_height = 480
additionx = 0
additiony = 0
snakebody = []
length_of_snake = 1
Gameactive = False
Gameclose = False
up = False
down = False
left = False
right = False
score = 0
goodbye = False
Allowed = False
snakeblock = 30

#setting up the screen
screen = pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption("Snake game")
clock = pygame.time.Clock()

#importing images
bg_image = pygame.image.load("INGAME BG.jpg").convert_alpha()
bg_image = pygame.transform.scale(bg_image,(dis_width,dis_height)).convert_alpha()
BG = pygame.image.load("BG.jpg").convert_alpha()
BG = pygame.transform.scale(BG,(dis_width, dis_height)).convert_alpha()

#Importing sounds
foodsound = pygame.mixer.Sound("FOODSOUND.wav")
deathsound = pygame.mixer.Sound("DEATHSOUND.mp3")

#define x and y pos for snake and food
snake_x = random.randint(1,dis_width// snakeblock) * snakeblock
snake_y = random.randint(1,dis_height// snakeblock) * snakeblock
foodx = random.randint(1,(dis_width-5) //snakeblock) * snakeblock
foody = random.randint(1,(dis_height-5) //snakeblock) * snakeblock

#Creating texts for the game
font = pygame.font.Font(None, 50)
welcome_txt = font.render("Welcome to snake game",False,"black")
welcome_Rect = welcome_txt.get_rect(center=(340,240))
instruct = font.render("press x to start or Q to quit..",False,"red")
instruct_rect = instruct.get_rect(center=(340,210))
gameover = font.render("Game over!",False,"Green")
gameover_rect = gameover.get_rect(center=(360,150))

while not Gameclose:
  if goodbye == False:
      screen.blit(BG, (0, 0))
      screen.blit(welcome_txt,welcome_Rect)
      screen.blit(instruct,instruct_rect)
      pygame.display.update()
      clock.tick(5)
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              pygame.quit()
              exit()
          if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_x:
                  Gameactive = True
              elif event.key == pygame.K_q:
                  Gameclose = True
      while Gameactive:
          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  pygame.quit()
                  exit()
              #Handling input
              if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_w and not down:
                       up = True
                       down = False
                       right = False
                       left = False
                       additiony =- snakeblock
                       additionx = 0
                       Allowed = True
                  elif event.key == pygame.K_d and not left:
                       right = True
                       left = False
                       up = False
                       down = False
                       additionx = snakeblock
                       additiony = 0
                       Allowed = True
                  elif event.key == pygame.K_a and not right:
                       left = True
                       right = False
                       up = False
                       down = False
                       additionx =- snakeblock
                       additiony = 0
                       Allowed = True
                  elif event.key == pygame.K_s and not up:
                       down = True
                       up = False
                       right = False
                       left = False
                       additiony = snakeblock
                       additionx = 0
                       Allowed = True
          if Allowed:
              snake_x += additionx
              snake_y += additiony
          screen.blit(bg_image, (0, 0))
          pygame.draw.rect(screen, "orange", [foodx, foody, snakeblock, snakeblock])
          snakehead = []
          snakehead.append(snake_x)
          snakehead.append(snake_y)
          snakebody.append(snakehead)
          #collision with walls
          if snake_x < 0 or snake_y > 477 or snake_y < 0 or snake_x > 717:
               deathsound.play()
               time.sleep(3)
               goodbye = True
               Gameactive = False
          if len(snakebody) > length_of_snake:
              del snakebody[0]
          #collision of snake with itself
          for x in snakebody[:-1]:
              if x == snakehead:
                 deathsound.play()
                 time.sleep(3)
                 goodbye = True
                 Gameactive = False
                 Allowed = False
          #drawing snake's body
          for x in snakebody:
                pygame.draw.rect(screen, "black", pygame.Rect(x[0], x[1], snakeblock, snakeblock))
                pygame.draw.rect(screen,"red",pygame.Rect(x[0],x[1],snakeblock,snakeblock),2)
          if snake_x == foodx and snake_y == foody:
               score += 10
               foodsound.play()
               foodx = random.randint(1, (dis_width - 5)// snakeblock)  * snakeblock
               foody = random.randint(1, (dis_height - 5) // snakeblock) * snakeblock
               for x in range(0,len(snakebody)):
                   if snakebody[x][0] == foodx and snakebody[x][1] == foody:
                       foodx = random.randint(1, (dis_width - 5) // snakeblock) * snakeblock
                       foody = random.randint(1, (dis_height - 5) // snakeblock) * snakeblock
               length_of_snake += 1
          showscore(score)
          pygame.display.update()
          clock.tick(10)
  else:
     screen.blit(BG,(0,0))
     screen.blit(gameover,gameover_rect)
     screen.blit(instruct,instruct_rect)
     SC = font.render(f"Your score: {score}",False,"Green")
     SC_rect = SC.get_rect(center=(360,180))
     screen.blit(SC,SC_rect)
     pygame.display.update()
     clock.tick(5)
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
             exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
               snake_x = random.randint(1, dis_width // snakeblock) * snakeblock
               snake_y = random.randint(1, dis_height // snakeblock) * snakeblock
               score = 0
               snakebody.clear()
               length_of_snake = 1
               goodbye = False
               Gameactive = True
               up = False
               down = False
               left = False
               right = False
               Allowed = False
            elif event.key==pygame.K_q:
               Gameclose = True
