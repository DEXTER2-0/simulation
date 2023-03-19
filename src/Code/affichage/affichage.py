from Threading import thread 
import time 
from math import *
import pygame
from .. import simulation 
import os

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


	

	def boucle(self,fps):
		""" 	Cette boucle permet d'actualiser l'affichage a chaque pas de temps   """

		self.run = True

		while self.run : 
			self.update()
			time.sleep(1./fps)
	


	def events(self) :
		""" sert a recuperer les evenements """

		for event in pygame.event.get() : 
			if event.type == pygame.QUIT:
				pygame.quit()
				exit(0)
			elif event.type == pygame.KEYDOWN :
				self.pressed[event.key] = True
			elif event.type == pygame.KEYUP : 
				self.pressed[event.key] = False 



	def update(self,fps):

		""" Permet de réafficher et de redessiner le robot et les obstacles """

		#dessiner la balise : 

		self._screen.blit(self._trace, (0, 0))
		#dessiner les obstacles : 

		for obs in self.simulation.terrain.getListeObstacles():
			pygame.draw.circle(self._trace, RED, (obs.x + self._screen.get_size()[0]/2, obs.y + self._screen.get_size()[0]/2), obs.rayon)





	       #on dessine le robot : 

	       os.chdir(os.path.dirname(os.path.abspath(__file__)))
	       im1 = pygame.image.load("robot.png").convert_alpha()
	       im1 = pygame.transform.scale(image_pas_tournee, (image_pas_tournee.get_width()/20 * robot.rayonDuRobotCm, im1.get_height()/20 * robot.rayonDuRobotCm))

	       im2 = pygame.transform.rotate(im1, degrees(robot.angle))


	       #affichage du robot : 
	       pygame.draw.circle(self._trace, GREEN, (robot.x + self._trace.get_size()[0]/2, robot.y + self._trace.get_size()[0]/2), 2)

	       #mettre a jour l'ecran 

	       pygame.display.update()

	       #femeture de la fenetre :
	       self.events()




