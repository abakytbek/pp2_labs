import pygame

pygame.init()

width, height = 300, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Red ball")

white = (255, 255, 255)
red = (255, 0, 0)

radius = 25
x = width // 2
y = height // 2
step = 20

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(white)
    pygame.draw.circle(screen, red, (x, y), radius)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            nx, ny = x, y

            if event.key == pygame.K_UP:
                ny -= step
            if event.key == pygame.K_DOWN:
                ny += step
            if event.key == pygame.K_LEFT:
                nx -= step
            if event.key == pygame.K_RIGHT:
                nx += step

            if radius <= nx <= width - radius:
                x = nx
            if radius <= ny <= height - radius:
                y = ny

    pygame.display.flip()
    clock.tick(60)

pygame.quit()