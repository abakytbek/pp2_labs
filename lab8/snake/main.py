import pygame, sys
import random, time

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
TILE_SIZE = 20

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')

font_small = pygame.font.SysFont('Verdana', 25)
font_big = pygame.font.SysFont('Verdana', 40)

snake = [(100, 100), (80, 100), (60, 100)]
direction = "RIGHT"
new_direction = direction

fposition = (200, 200)
fspawn = True
fvalue = 1
fcolor = RED
ftimer = 0
flifetime = 5000

score = 0
level = 1
speed = 10

clock = pygame.time.Clock()

def show_score_level():
    score_text = font_small.render(f"Score: {score}", True, BLACK)
    level_text = font_small.render(f"Level: {level}", True, BLACK)
    DISPLAYSURF.blit(score_text, (10, 10))
    DISPLAYSURF.blit(level_text, (SCREEN_WIDTH - 100, 10))

def game_over():
    text = font_big.render("Game Over", True, RED)
    DISPLAYSURF.blit(text, (90, 150))
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    sys.exit()

def generate_food():
    global fvalue, fcolor, ftimer
    fvalue = random.choice([1, 2, 3, 5])

    if fvalue == 1:
        fcolor = RED
    elif fvalue == 2:
        fcolor = ORANGE
    elif fvalue == 3:
        fcolor = YELLOW
    else:
        fcolor = BLUE

    while True:
        x = random.randrange(0, SCREEN_WIDTH - TILE_SIZE, TILE_SIZE)
        y = random.randrange(0, SCREEN_HEIGHT - TILE_SIZE, TILE_SIZE)
        if (x, y) not in snake:
            break

    ftimer = pygame.time.get_ticks()
    return (x, y)

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                new_direction = "UP"
            if event.key == pygame.K_DOWN:
                new_direction = "DOWN"
            if event.key == pygame.K_LEFT:
                new_direction = "LEFT"
            if event.key == pygame.K_RIGHT:
                new_direction = "RIGHT"

    if new_direction == "UP" and direction != "DOWN":
        direction = "UP"
    if new_direction == "DOWN" and direction != "UP":
        direction = "DOWN"
    if new_direction == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    if new_direction == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"

    x, y = snake[0]
    if direction == "UP":
        y -= TILE_SIZE
    if direction == "DOWN":
        y += TILE_SIZE
    if direction == "LEFT":
        x -= TILE_SIZE
    if direction == "RIGHT":
        x += TILE_SIZE

    snake_head = (x, y)
    snake.insert(0, snake_head)

    if x < 0 or x >= SCREEN_WIDTH or y < 0 or y >= SCREEN_HEIGHT:
        game_over()

    if snake_head in snake[1:]:
        game_over()

    if snake_head == fposition:
        score += fvalue
        fspawn = False

        if score % 10 == 0:
            level += 1
            speed += 2
    else:
        snake.pop()

    if pygame.time.get_ticks() - ftimer > flifetime:
        fspawn = False

    if not fspawn:
        fposition = generate_food()
        fspawn = True

    DISPLAYSURF.fill(WHITE)

    for pos in snake:
        pygame.draw.rect(DISPLAYSURF, GREEN, (pos[0], pos[1], TILE_SIZE, TILE_SIZE))

    pygame.draw.rect(DISPLAYSURF, fcolor, (fposition[0], fposition[1], TILE_SIZE, TILE_SIZE))

    show_score_level()
    pygame.display.update()
    clock.tick(speed)
