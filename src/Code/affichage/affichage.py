from threading import Thread 
import time 
from math import *
import pygame 
import logging
from Code.simulation import constantes as cs
from copy import deepcopy

#colors 
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
AUTRE = (235, 152, 135)

class CircSprite(pygame.sprite.Sprite):
    """
    Représente le sprite d'un cercle
    """
    def __init__(self, color, pos, rayon, t):
        super().__init__()
        self.type = t # Debug information
        self.image = pygame.Surface([2*rayon, 2*rayon])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        # TODO: Will be modified later to support other types of obstacles
        pygame.draw.circle(self.image, color, (rayon, rayon), rayon)
        self.rect = self.image.get_rect(center=pos)

class Affichage(Thread):
	def __init__(self, simulation,fps):
		""" 
		Constructeur de la classe affichage
		:param simulation : simulation choisie
		:param terrain : terrain choisi
		:param robot : robot choisi
		:param fps :
		"""
		super(Affichage, self).__init__()
		self.simulation = simulation
		pygame.init()
		self.disp = pygame.display.set_mode((cs.WIDTH, cs.HEIGHT))
		self.disp.fill(cs.WHITE)
		self.fps = fps
		self.old_pos=[]
		self.clock = pygame.time.Clock()
		logging.info("Affichage cree")

	def run(self):
		""" 	
		Cette boucle permet d'actualiser l'affichage a chaque pas de temps   
		"""
		self.encours= True
		while self.encours : 
			self.update()
			self.clock.tick(self.fps)
		pygame.quit()
		self.simulation.stop()
		logging.info("Affichage terminé")
	
	def events(self) :
		""" 
		sert a recuperer les evenements 
		"""
		for event in pygame.event.get() : 
			if event.type == pygame.QUIT:
				self.encours = False
			elif event.type == pygame.KEYDOWN :
				if event.key in [pygame.K_ESCAPE, pygame.K_q]: #Quit
					self.encours = False
				if event.key in [pygame.K_d]: 
					logging.debug(f"List of sprites :")
					for sprite in self.sprites:
						logging.debug(f"\t{sprite.type} : {{{sprite.rect.x},{sprite.rect.y}}}")

	def update(self):
		"""
        Met à jour la position des sprites
        """
		self.robot.rect.x = self.simulation.pos_x + self.mid
		self.robot.rect.y = self.simulation.pos_y + self.mid
		self.sprites.update()
		self._screen.fill(WHITE)
		self.sprites.draw(self._screen)
		pygame.display.flip()
		self.events()
