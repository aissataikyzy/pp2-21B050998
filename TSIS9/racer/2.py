#Imports
import pygame, sys, time
from pygame.locals import *
from random import randint

# Functionallity, which added from student 
#___________________
'''
SOME CODE
'''
#___________________

#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (randint(40,SCREEN_WIDTH-40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (randint(40, SCREEN_WIDTH - 40), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)

#___________________
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.value_container = [1, 2, 5]
        self.image_container = ['Coin.png', 'Coin1.png', 'Coin2.png']
        self.current = randint(0, 2)
        self.image = pygame.image.load(self.image_container[self.current])
        self.image = pygame.transform.scale(self.image, (35, 35))
        self.rect = self.image.get_rect()
        self.rect.center = (randint(40,SCREEN_WIDTH-40), 0)
        self.speed = randint(2, 5)
    
    def move(self):
        self.rect.move_ip(0, self.speed)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (randint(40, SCREEN_WIDTH - 40), 0)

            self.current = randint(0, 2)
            self.image = pygame.image.load(self.image_container[self.current])
            self.image = pygame.transform.scale(self.image, (35, 35))
#___________________
                  

#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
rewards = pygame.sprite.Group()
rewards.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

#Adding and playing infinitely music
#___________________
pygame.mixer.music.load("week10_materials_background.wav")
pygame.mixer.music.play(-1)
#___________________

#Game Loop
while True:
      
    #Cycles through all events occuring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.3
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    #___________________
    coins = font_small.render(str(COINS), True, BLACK)
    DISPLAYSURF.blit(coins, (370,10))
    #___________________

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
        

    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('week10_materials_crash.wav').play()
        time.sleep(1)
                
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30,250))
        coin_result = font_small.render('Coins collected ' + str(COINS), True, BLACK)
        DISPLAYSURF.blit(coin_result, (110, 350))
        
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(5)
        pygame.quit()
        sys.exit()   

    #To be run if collision occurs between Player and Coins
    #___________________
    collected_coins = pygame.sprite.spritecollide(P1, rewards, True)
    for coin in collected_coins:
        COINS += coin.value_container[coin.current]

        if COINS % 15 == 0 and COINS != 0:
            SPEED += 1

        rewards.remove(coin)
        coin.kill()
        C1 = Coin()
        all_sprites.add(C1)
        rewards.add(C1)
    #___________________

    pygame.display.update()
    FramePerSec.tick(FPS)
