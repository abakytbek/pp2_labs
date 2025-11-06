import pygame, sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    tool = 'brush'  ##
    points = []
    
    start_pos = None

    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            # выход из программы
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held: return
                if event.key == pygame.K_F4 and alt_held: return
                if event.key == pygame.K_ESCAPE: return

                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'

                ##
                elif event.key == pygame.K_p: #прямоугольник
                    tool = 'rect'
                elif event.key == pygame.K_c: #круг
                    tool = 'circle'
                elif event.key == pygame.K_t: #кисть тул
                    tool = 'brush'
                elif event.key == pygame.K_e: #ластик
                    tool = 'eraser'

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if tool in ['rect', 'circle']:
                        start_pos = event.pos ##начало фигуры
                if event.button == 3: #правая кнопка умен радиус
                    radius = max(1, radius - 1)
                elif event.button == 2: #средняя кнопка увел радиус
                    radius = min(200, radius + 1)

            if event.type == pygame.MOUSEBUTTONUP:
                if tool == 'rect' and start_pos:
                    end_pos = event.pos
                    rect = pygame.Rect(start_pos, (end_pos[0]-start_pos[0], end_pos[1]-start_pos[1]))
                    pygame.draw.rect(screen, get_color(mode), rect, 2)
                elif tool == 'circle' and start_pos:
                    end_pos = event.pos
                    r = int(((end_pos[0]-start_pos[0])**2 + (end_pos[1]-start_pos[1])**2)**0.5)
                    pygame.draw.circle(screen, get_color(mode), start_pos, r, 2)
                start_pos = None

            if event.type == pygame.MOUSEMOTION:
                if tool == 'brush' and event.buttons[0]:
                    position = event.pos
                    points.append(position)
                    points = points[-256:]
                elif tool == 'eraser' and event.buttons[0]:
                    pygame.draw.circle(screen, (0,0,0), event.pos, radius)

        if tool == 'brush':
            i = 0
            while i < len(points) - 1:
                drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
                i += 1

        pygame.display.flip()
        clock.tick(60)


def get_color(color_mode):
    if color_mode == 'blue':
        return (0, 0, 255)
    elif color_mode == 'red':
        return (255, 0, 0)
    elif color_mode == 'green':
        return (0, 255, 0)
    else:
        return (255, 255, 255)

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))

    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

main()
