import pygame
import datetime

pygame.init()

width, height = 900, 900
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Micky clockapp")

clock = pygame.time.Clock()

background = pygame.image.load("base_micky.jpg")
minhand = pygame.image.load("minute.png").convert_alpha()
sechand = pygame.image.load("second.png").convert_alpha()

background = pygame.transform.smoothscale(background, (width + 100, height - 50))

center = (width // 2, height // 2)
x = 46
y = -21

def draw_hand(image, angle):
    rotated = pygame.transform.rotate(image, -angle)
    rect = rotated.get_rect(center=(center[0] + x, center[1] + y))
    screen.blit(rotated, rect)

run = True
while run:
    for do in pygame.event.get():
        if do.type == pygame.QUIT:
            run = False

    now = datetime.datetime.now()
    sec = now.second  # dlya plavnosti /1e6
    minute = now.minute  # sec / 60

    secangle = (sec / 60) * 360
    minangle = (minute / 60) * 360
    minangle += 50

    screen.blit(background, (0, 0))
    draw_hand(minhand, minangle)
    draw_hand(sechand, secangle)

    pygame.display.flip()
    clock.tick(60)
