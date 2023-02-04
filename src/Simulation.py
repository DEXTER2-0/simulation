from Robot import *
from Obstacle import *
from Roue import *
from Capteur_de_distance import *

class Simulation :
    def __init__ (self, rayonRouesCm,rayonDuRobotCm, capteurDistance,vMaxTourParSec) :
        """
        """
        mur_x = 10
        mur_y = 10
        self.robot = Robot(rayonRouesCm, rayonDuRobotCm, capteurDistance, vMaxTourParSec)
        obs1 = Obstacle(6,2,2)
        obs2 = Obstacle(3,4,7,6)

    





