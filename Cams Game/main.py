# Pygame basic template

import pygame, os
from pygame.locals import *

pygame.init()

while True:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            os._exit(0)