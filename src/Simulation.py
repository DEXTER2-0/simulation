from Robot import *
from Obstacle import *
from Roue import *
from Capteur_de_distance import *

class Simulation :
	def __init__ (self, rayonRouesCm,rayonDuRobotCm, capteurDistance,vMaxTourParSec) :
		"""
		"""
		self.robot = Robot(rayonRouesCm, rayonDuRobotCm, capteurDistance, vMaxTourParSec)
        





