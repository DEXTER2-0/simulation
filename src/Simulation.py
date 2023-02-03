from Roue import *
from Obscle import *
from Roue import *
from Capteur_de_distance import *

class Simulation :
	def __init__ (self, terrain, nbObstacle, rayonRouesCm,rayonDuRobotCm, capteurDistance,vMaxTourParSec) :
		"""
		"""
		self.terrain = terrain
		self.robot = Robot(rayonRouesCm, rayonDuRobotCm, capteurDistance, vMaxTourParSec)
        cpt = 1
        self.listObs = dict()
        #while(cle<=nbstacle): 
            #valX = 
            #valY = 
            #self.listOns[cpt] = Obstacle(10,)


