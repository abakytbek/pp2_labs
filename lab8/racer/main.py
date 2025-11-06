import pygame, sys # импортируем для игры и выхода
from pygame.locals import * #импортируем все константы pygame
import random, time #случ числа и тайм для пауз

pygame.init() 

FPS = 60
FramePerSec = pygame.time.Clock()

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0    ##

#шрифт и текст
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")

DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

class Enemy(pygame.sprite.Sprite):
      def __init__(self): #конструктор
        super().__init__() #вызываем род класс
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40),0) #случ - вставка врага

      def move(self): #метод для движения врага
        global SCORE
        self.rect.move_ip(0,SPEED) #враг движется вниз
        if (self.rect.top > 600): #если враг уходит вниз(край) то добавляем очки
            SCORE += 1
            self.rect.top = 0 #возврат наверх
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40),0) # новая случ вставка


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0: #если игрок не уходит за левый край
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0) #двиэение влево
        if self.rect.right < SCREEN_WIDTH:     
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)


#
class Coin(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Coin.png")
        self.image = pygame.transform.scale(self.image, (40, 40)) #размер монетки
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40),0)

      def move(self):
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600): #если монета вышла за экран
            self.rect.top = 0 #вернуть наверх
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40),0)


P1 = Player()
E1 = Enemy()
C1 = Coin() #

enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group() #
coins.add(C1)

all_sprites = pygame.sprite.Group() # группа всех обьектов
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

INC_SPEED = pygame.USEREVENT + 1 #увел скорости
pygame.time.set_timer(INC_SPEED, 1000) #каждую сек

while True:
      
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5      
        if event.type == QUIT:
            pygame.quit()
            sys.exit() #выход из прог


    DISPLAYSURF.blit(background, (0,0)) #фон
    scores = font_small.render(str(SCORE), True, BLACK) #очки
    DISPLAYSURF.blit(scores, (10,10)) #рисовка очков

    coins_text = font_small.render("Coins: " + str(COINS), True, BLACK) ##
    DISPLAYSURF.blit(coins_text, (300,10)) 

    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect) #рисуем на экране
        entity.move() #двиг обьект

    ##
    if pygame.sprite.spritecollideany(P1, coins): #касание монеты
        COINS += 1
        for coin in coins:
            coin.rect.top = 0 #вернуть наверх
            coin.rect.center = (random.randint(40, SCREEN_WIDTH - 40),0)

    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('crash.wav').play()
          time.sleep(0.5)
                   
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
          
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() #удаляем все обьекты
          time.sleep(2) #ожидание сек
          pygame.quit()
          sys.exit()        
        
    pygame.display.update()
    FramePerSec.tick(FPS)
