from threading import Thread 
import time 
from math import *
import pygame 
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
	def __init__(self, simulation,terrain,robot,fps):
		""" Constructeur de la classe affichage """

		super(Affichage, self).__init__()
		self.simulation = simulation
		pygame.init()
		self.terrain = terrain
		self.robot=robot
		self._trace = pygame.surface.Surface(((self.terrain.WIDTH_MAX*2)+self.robot.rayonDuRobotCm*2 , (self.terrain.HEIGHT_MAX*2)+self.robot.rayonDuRobotCm*2))
		self._screen = pygame.display.set_mode(((self.terrain.WIDTH_MAX*2)+self.robot.rayonDuRobotCm*2, (self.terrain.HEIGHT_MAX*2)+self.robot.rayonDuRobotCm*2))
		self._screen.fill((255, 255, 255))
		self._trace.fill((255, 255, 255))
		self.fps = fps 


	

	def run(self):
		""" 	Cette boucle permet d'actualiser l'affichage a chaque pas de temps   """

		self.encours= True

		while self.encours : 
			self.update(self.fps)
			time.sleep(1./self.fps)
	


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
			pygame.draw.circle(self._trace, RED, (obs.x + self._screen.get_size()[0]/2, obs.y + self._screen.get_size()[0]/2), obs.longueur)
		#os.chdir(os.path.dirname(os.path.abspath(__file__)))
		#im1 = pygame.image.load("robot.png").convert_alpha()
		#im1 = pygame.transform.scale(im1, (im1.get_width()/10 * self.robot.rayonDuRobotCm, im1.get_height()/10 * self.robot.rayonDuRobotCm))
			#im2 = pygame.transform.rotate(im1, degrees(self.simulation.getangle()))
		pygame.draw.circle(self._trace, GREEN, (self.simulation.pos_x + self._trace.get_size()[0]/2, self.simulation.pos_y + self._trace.get_size()[0]/2),self.robot.rayonDuRobotCm)
		pygame.display.update()
		self.events()

		

