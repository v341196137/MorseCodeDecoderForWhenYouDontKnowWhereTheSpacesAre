import pygame

pygame.init()
screen = pygame.display.set_mode((790, 300))
pygame.display.set_caption("Hello, World!")
running = True

world = []
ends = []
ends.append('|')
for j in range(0, 79 - 2):
    ends.append('-')
ends.append('|')
world.append(ends)
for i in range(0, 30 - 2):
    line = []
    line.append('|')
    for j in range(0, 79 - 2):
        line.append(' ')
    line.append('|')
    world.append(line)
world.append(ends)

build = "room"

last_pos = (0, 0)
def mark_room(last_pos, pos):
    x1 = min(last_pos[0], pos[0])//10
    x2 = max(last_pos[0], pos[0])//10
    y1 = min(last_pos[1], pos[1])//10
    y2 = max(last_pos[1], pos[1])//10
    
    world[y1][x1] = '|'
    world[y1][x2] = '|'
    world[y2][x1] = '|'
    world[y2][x2] = '|'

    for i in range(x1 + 1, x2):
        world[y1][i] = '-'
        world[y2][i] = '-'
   
    for i in range(y1 + 1, y2):
        world[i][x1] = '|'
        for j in range(x1 + 1, x2):
            world[i][j] = '.'
        world[i][x2] = '|'

def mark_empty(last_pos, pos):
    x1 = min(last_pos[0], pos[0])//10
    x2 = max(last_pos[0], pos[0])//10
    y1 = min(last_pos[1], pos[1])//10
    y2 = max(last_pos[1], pos[1])//10
    for i in range(y1, y2):
        for j in range(x1, x2):
            world[i][j] = ' '

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            x = pos[0]//10
            y = pos[1]//10
            if build == "room":
                mark_room(last_pos, pos)
            elif build == "passage":
                world[y][x] = '#'
            elif build == "door":
                world[y][x] = '+'
            elif build == "vertical_wall":
                world[y][x] = '|'
            elif build == "horizontal_wall":
                world[y][x] = '-'
            elif build == "inside":
                world[y][x] = '.'
            elif build == "empty":
                mark_empty(last_pos, pos)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if build == "room" or build == "empty":
                last_pos = pygame.mouse.get_pos()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                build = "room"
            elif event.key == pygame.K_p:
                build = "passage"
            elif event.key == pygame.K_d:
                build = "door"
            elif event.key == pygame.K_v:
                build = "vertical_wall"
            elif event.key == pygame.K_h:
                build = "horizontal_wall"
            elif event.key == pygame.K_i:
                build = "inside"
            elif event.key == pygame.K_e:
                build = "empty"
            
    for i in range(len(world)):
        for j in range(len(world[i])):
            color = (0, 0, 0)
            width = 0
            if world[i][j] == '-' or world[i][j] == '|':
                color = (100, 100, 100)
            elif world[i][j] == '.':
                color = (255, 255, 255)
            elif world[i][j] == '#':
                color = (0, 0, 255)
            elif world[i][j] == '+':
                color = (255, 0, 0)
            pygame.draw.rect(screen, color, (j * 10, i * 10, 10, 10), width)
    pygame.display.flip()

pygame.quit()
with open('world.txt', 'w') as f:
    for i in range(len(world)):
        for j in range(len(world[i])):
            f.write(world[i][j])
        f.write('\n')
