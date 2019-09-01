import pygame
import sys
import time
import random

error = pygame.init()
if error[1] > 0:
    print(error)
    sys.exit(-1)

width = 18
height = 12
blksz = 20

screen = pygame.display.set_mode((width*blksz, height*blksz))
pygame.display.set_caption('Snake')

dot_color = pygame.Color(255, 0, 0)
bg_color = pygame.Color(0, 255, 255)
food_color = pygame.Color(0, 0, 255)
dead_color = pygame.Color(255, 0, 255)

clock = pygame.time.Clock()

mp = [[0 for i in range(height)] for j in range(width)]
x = 0
y = 0
dx = 1
dy = 0
length = 10
extend = 0
mp[random.randrange(width)][random.randrange(height)] = -1

while True:
    # dispatch input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                dx = 1
                dy = 0
            elif event.key == pygame.K_LEFT:
                dx = -1
                dy = 0
            elif event.key == pygame.K_UP:
                dx = 0
                dy = -1
            elif event.key == pygame.K_DOWN:
                dx = 0
                dy = 1
            elif event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    # snake go advance
    if mp[x][y] != -2:
        x = (x + dx + width) % width
        y = (y + dy + height) % height
        if mp[x][y] == -1:
            # extend when catch food
            extend = 1
            length += 1
            mp[x][y] = length
            # replace food
            mp[random.randrange(width)][random.randrange(height)] = -1
        elif mp[x][y] == 0:
            # normal advance
            extend = 0
            mp[x][y] = length
        else:
            # collision with own body and stop
            extend = 1
            mp[x][y] = -2

    # draw client area
    for i in range(width):
        for j in range(height):
            if mp[i][j] == -2:
                # draw collision
                pygame.draw.rect(screen, dead_color, pygame.Rect(i*blksz, j*blksz, blksz, blksz))
            elif mp[i][j] == -1:
                # draw food
                pygame.draw.rect(screen, food_color, pygame.Rect(i*blksz, j*blksz, blksz, blksz))
            elif mp[i][j] != 0:
                # draw snake body and decrease its life displayed
                if extend == 0:
                    mp[i][j] -= 1
                pygame.draw.rect(screen, dot_color, pygame.Rect(i*blksz, j*blksz, blksz, blksz))
            else:
                # unoccupied space
                pygame.draw.rect(screen, bg_color, pygame.Rect(i*blksz, j*blksz, blksz, blksz))

    # flip buffer and wait
    pygame.display.flip()
    clock.tick(5)