from threading import Thread 
import time 
from math import *
import pygame 

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
		self._trace = pygame.surface.Surface((self.simulation.terrain.WIDTH_MAX , self.simulation.terrain.HEIGHT_MAX))
		self._screen = pygame.display.set_mode((self.simulation.terrain.WIDTH_MAX , self.simulation.terrain.HEIGHT_MAX))
		self._screen.fill((255, 255, 255))
		self._trace.fill((255, 255, 255))
		self.fps = fps
		self.mid = self.simulation.terrain.WIDTH_MAX / 2
		self.sprites = pygame.sprite.Group()
		self.robot = CircSprite(GREEN, (self.simulation.pos_x + self.mid, self.simulation.pos_y + self.mid), self.simulation.robot.rayonDuRobotCm, "Robot")
		self.sprites.add(self.robot)
		for obs in self.simulation.terrain.getListeObstacles():
			self.sprites.add(CircSprite(RED, (obs.x + self.mid, obs.y + self.mid), obs.longueur, "Obstacle"))
		self.clock = pygame.time.Clock()

	def run(self):
		""" 	
		Cette boucle permet d'actualiser l'affichage a chaque pas de temps   
		"""
		self.encours= True
		while self.encours : 
			self.update()
			self.clock.tick(self.fps)
		pygame.quit()
	
	def events(self) :
		""" 
		sert a recuperer les evenements 
		"""
		for event in pygame.event.get() : 
			if event.type == pygame.QUIT:
				self.running = False
			elif event.type == pygame.KEYDOWN :
				if event.key in [pygame.K_ESCAPE, pygame.K_q]:
					self.encours = False

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
