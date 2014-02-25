## Basic pygame animation

# Import modules
import pygame, os
from pygame.locals import *

# Activate pygame
pygame.init()
pygame.display.set_caption("Basic Animation Test")

# Game window
DISPLAYSURF = pygame.display.set_mode((640, 480), 0, 32)

# Load images
# Ball one
ball_load = pygame.image.load("ball_01.png")
ball = ball_load.convert_alpha()
ball_x = ball.get_width()
ball_y = (DISPLAYSURF.get_height() / 4) * 0.5

# Ball two 
ball_2_load = pygame.image.load("ball_02.png")
ball_2 = ball_2_load.convert_alpha()
ball_2_x = ball_2.get_width()
ball_2_y = (DISPLAYSURF.get_height() / 4) * 2.5

#Variables
COLOR = (0, 0, 0)
x = 0
x_2 = 640 - ball_2_x
clock = pygame.time.Clock()

# Events function
def input_events(events):
    for event in events:
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            os._exit(0)

while True:
    clock.tick(30) #The game runs at 30 ticks per second
    input_events(pygame.event.get())

    DISPLAYSURF.fill(COLOR)
    DISPLAYSURF.blit(ball, (x, ball_y))
    DISPLAYSURF.blit(ball_2, (x_2, ball_2_y))

    x += 1
    x_2 -= 1

    if x > 640:
        x = 0 - ball_x

    if x_2 < 0 - ball_2_x:
        x_2 = 640 
        
    pygame.display.update()
