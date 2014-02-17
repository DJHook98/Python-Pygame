# *Untiled* pygame file

import pygame, os, random
from pygame.locals import *

# Initiate PyGame 
pygame.init()

#Clock setting


# Class tests
class Player(pygame.sprite.Sprite):

	image = pygame.image.load("graphics/player/player-idle.png")
	image = image.convert_alpha()

	def __init__(self, startpos):
		pygame.sprite.Sprite.__init__(self, self.groups)
		self.pos = startpos
		self.image = Player.image
		self.rect = self.image.get_rect()

	def update(self):
		self.rect.center = self.pos
