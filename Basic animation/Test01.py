## Basic pygame animation

# Import modules
import pygame, os
from pygame.locals import *

# Activate pygame
pygame.init()

# Game window
DISPLAYSURF = pygame.display.set_mode((640, 480), 0, 32)

# Load images
ball_load = pygame.image.load("ball_01.png")
ball = ball_load.convert_alpha()
ball_x = ball.get_width()

#Variables
COLOR = (0, 0, 0)
x = 0

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            os._exit(0)

    DISPLAYSURF.fill(COLOR)
    DISPLAYSURF.blit(ball, (x, 160))

    x += 1

    if x > 640:
        x = 0 - ball_x

    pygame.display.update()
