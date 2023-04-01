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
		x,y=self.simulation.robot.center.x,self.simulation.robot.center.y
		self.old_pos.append((x,y))
		self.disp.fill(WHITE)
		for obs in self.simulation.terrain.listesobstacle :
			obs.draw(self.disp,RED)
		for pos in self.old_pos :
			pygame.draw.circle(self.disp,RED,pos,2)
		pygame.draw.circle(self.disp,BLUE,(x,y),self.simulation.robot.rayonDuRobotCm//10)
		pygame.display.flip()
		self.events()
