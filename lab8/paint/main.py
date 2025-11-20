import pygame, sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius = 15
    mode = 'blue'
    tool = 'brush'
    points = []
    start_pos = None

    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():

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

                elif event.key == pygame.K_p:
                    tool = 'rect'
                elif event.key == pygame.K_c:
                    tool = 'circle'
                elif event.key == pygame.K_t:
                    tool = 'brush'
                elif event.key == pygame.K_e:
                    tool = 'eraser'

                elif event.key == pygame.K_k:
                    tool = 'square'
                elif event.key == pygame.K_v:
                    tool = 'right_triangle'
                elif event.key == pygame.K_q:
                    tool = 'equilateral'
                elif event.key == pygame.K_h:
                    tool = 'rhombus'

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if tool in ['rect', 'circle', 'square', 'right_triangle', 'equilateral', 'rhombus']:
                        start_pos = event.pos
                if event.button == 3:
                    radius = max(1, radius - 1)
                elif event.button == 2:
                    radius = min(200, radius + 1)

            if event.type == pygame.MOUSEBUTTONUP:
                end_pos = event.pos

                if start_pos:
                    sx, sy = start_pos
                    ex, ey = end_pos

                    if tool == 'rect':
                        rect = pygame.Rect(start_pos, (ex - sx, ey - sy))
                        pygame.draw.rect(screen, get_color(mode), rect, 2)

                    elif tool == 'circle':
                        r = int(((ex - sx)**2 + (ey - sy)**2)**0.5)
                        pygame.draw.circle(screen, get_color(mode), start_pos, r, 2)

                    elif tool == 'square':
                        side = max(abs(ex - sx), abs(ey - sy))
                        rect = pygame.Rect(sx, sy, side, side)
                        pygame.draw.rect(screen, get_color(mode), rect, 2)

                    elif tool == 'right_triangle':
                        points_tri = [(sx, sy), (ex, sy), (sx, ey)]
                        pygame.draw.polygon(screen, get_color(mode), points_tri, 2)

                    elif tool == 'equilateral':
                        side = abs(ex - sx)
                        height = int((3**0.5)/2 * side)
                        p1 = (sx, sy)
                        p2 = (sx + side, sy)
                        p3 = (sx + side/2, sy - height)
                        pygame.draw.polygon(screen, get_color(mode), (p1, p2, p3), 2)

                    elif tool == 'rhombus':
                        dx = ex - sx
                        dy = ey - sy
                        p1 = (sx, sy - dy//2)
                        p2 = (sx + dx//2, sy)
                        p3 = (sx, sy + dy//2)
                        p4 = (sx - dx//2, sy)
                        pygame.draw.polygon(screen, get_color(mode), (p1, p2, p3, p4), 2)

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
        progress = i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

main()
