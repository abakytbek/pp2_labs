import pygame

pygame.init()
pygame.mixer.init()

playlist = ["90.mp3", "Night.mp3", "Power.mp3", "Feel so Good.mp3"]
current = 0
playing = True

pygame.mixer.music.load(playlist[current])
pygame.mixer.music.play()

width, height = 400, 135
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pompeya player")
font = pygame.font.SysFont("Arial", 24)

cover = pygame.image.load("album.png").convert_alpha()
cover = pygame.transform.scale(cover, (100, 100))

def text(txt, x, y, color=(255, 255, 255)):
    img = font.render(txt, True, color)
    screen.blit(img, (x, y))

run = True
while run:
    screen.fill((30, 30, 30))
    screen.blit(cover, (20, 20))
    text(f"Now: {playlist[current]}", 140, 30)

    for do in pygame.event.get():
        if do.type == pygame.QUIT:
            run = False

        if do.type == pygame.KEYDOWN:
            if do.key == pygame.K_w:
                if playing:
                    pygame.mixer.music.pause()
                    playing = False
                    print("The track is paused")
                else:
                    pygame.mixer.music.unpause()
                    playing = True
                    print("THE track is playing")

            elif do.key == pygame.K_s:
                pygame.mixer.music.stop()
                playing = False
                print("The track is stopped")

            elif do.key == pygame.K_d:
                current += 1
                if current >= len(playlist):
                    current = 0
                pygame.mixer.music.load(playlist[current])
                pygame.mixer.music.play()
                playing = True
                print(f"The next track: {playlist[current]}")

            elif do.key == pygame.K_a:
                current -= 1
                if current < 0:
                    current = len(playlist) - 1
                pygame.mixer.music.load(playlist[current])
                pygame.mixer.music.play()
                playing = True
                print(f"The previous track: {playlist[current]}")

    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()
