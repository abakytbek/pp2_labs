import pygame, sys
import random, time, json
import psycopg2
from config import load_config

pygame.init()

def get_connection():
    cfg = load_config()
    return psycopg2.connect(**cfg)

def get_or_create_user():
    username = input("Enter username: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, level FROM user_profile WHERE username=%s;", (username,))
    user = cur.fetchone()

    if user:
        print(f"Hi, {username} Your level: {user[1]}")
        uid, level = user
    else:
        cur.execute(
            "INSERT INTO user_profile(username, level) VALUES(%s, 1) RETURNING id, level;",
            (username,)
        )
        uid, level = cur.fetchone()
        conn.commit()
        print(f"New user created: {username} (level 1)")

    cur.close()
    conn.close()
    return uid, level

def save_game_state(user_id, score, snake, fposition, speed, level):
    state = json.dumps({
        "snake": snake,
        "food": fposition,
        "speed": speed,
        "level": level
    })

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO user_score (user_id, score, state)
        VALUES (%s, %s, %s);
    """, (user_id, score, state))

    conn.commit()
    cur.close()
    conn.close()
    print("Game is saved")

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

def generate_walls(level):
    walls = []

    if level == 1:
        return walls  

    if level == 2:
        for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
            walls.append((SCREEN_WIDTH // 2, y))

    if level == 3:
        for x in range(100, 300, TILE_SIZE):
            walls.append((x, 100))
            walls.append((x, 300))
        for y in range(100, 300, TILE_SIZE):
            walls.append((100, y))
            walls.append((300, y))

    if level >= 4:
        for x in range(0, SCREEN_WIDTH, TILE_SIZE):
            if x % 40 == 0:
                for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
                    if (x + y) % 60 == 0:
                        walls.append((x, y))

    return walls


def generate_food():
    global fvalue, fcolor, ftimer

    fvalue = random.choice([1, 2, 3, 5])
    fcolor = [RED, ORANGE, YELLOW, BLUE][[1,2,3,5].index(fvalue)]

    while True:
        x = random.randrange(0, SCREEN_WIDTH - TILE_SIZE, TILE_SIZE)
        y = random.randrange(0, SCREEN_HEIGHT - TILE_SIZE, TILE_SIZE)
        if (x, y) not in snake and (x, y) not in walls:
            break

    ftimer = pygame.time.get_ticks()
    return (x, y)


user_id, level = get_or_create_user()
speed = 8 + level * 2
walls = generate_walls(level)

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

clock = pygame.time.Clock()

def show_info():
    score_text = font_small.render(f"Score: {score}", True, BLACK)
    level_text = font_small.render(f"Level: {level}", True, BLACK)
    DISPLAYSURF.blit(score_text, (10, 10))
    DISPLAYSURF.blit(level_text, (SCREEN_WIDTH - 110, 10))

def game_over():
    text = font_big.render("Game Over", True, RED)
    DISPLAYSURF.blit(text, (90, 150))
    pygame.display.flip()
    time.sleep(2)
    save_game_state(user_id, score, snake, fposition, speed, level)
    pygame.quit()
    sys.exit()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_game_state(user_id, score, snake, fposition, speed, level)
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                print("Game is saved")
                save_game_state(user_id, score, snake, fposition, speed, level)

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
    if direction == "UP": y -= TILE_SIZE
    if direction == "DOWN": y += TILE_SIZE
    if direction == "LEFT": x -= TILE_SIZE
    if direction == "RIGHT": y += 0 if direction == "RIGHT" else None

    if direction == "RIGHT":
        x += TILE_SIZE

    snake_head = (x, y)
    snake.insert(0, snake_head)

    if x < 0 or x >= SCREEN_WIDTH or y < 0 or y >= SCREEN_HEIGHT:
        game_over()

    if snake_head in snake[1:]:
        game_over()

    if snake_head in walls:
        game_over()

    if snake_head == fposition:
        score += fvalue
        fspawn = False
    else:
        snake.pop()

    if pygame.time.get_ticks() - ftimer > flifetime:
        fspawn = False

    if not fspawn:
        fposition = generate_food()
        fspawn = True

    DISPLAYSURF.fill(WHITE)

    for wx, wy in walls:
        pygame.draw.rect(DISPLAYSURF, BLACK, (wx, wy, TILE_SIZE, TILE_SIZE))

    for pos in snake:
        pygame.draw.rect(DISPLAYSURF, GREEN, (pos[0], pos[1], TILE_SIZE, TILE_SIZE))

    pygame.draw.rect(DISPLAYSURF, fcolor, (fposition[0], fposition[1], TILE_SIZE, TILE_SIZE))

    show_info()
    pygame.display.update()
    clock.tick(speed)
