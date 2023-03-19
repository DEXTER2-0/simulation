from Threading import thread 
import time 
from math import *
import pygame
from .. import simulation 

#colors 
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
AUTRE = (235, 152, 135)


class Affichage(Thread):
	def __init__(self, simulation):
		""" Constructeur de la classe affichage """

		super(Affichage, self).__init__()
		self.simulation = simulation
		pygame.init()
		self._trace = pygame.surface.Surface((simulation.terrain.WIDTH_MAX , simulation.terrain.HEIGHT_MAX))
		self._screen = pygame.display.set_mode((simulation.terrain.WIDTH_MAX , simulation.terrain.HEIGHT_MAX))
		self._screen.fill((255, 255, 255))
		self._trace.fill((255, 255, 255))


	




