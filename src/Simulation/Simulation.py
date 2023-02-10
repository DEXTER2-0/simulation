from Robot import *
from Obstacle import *
from Roue import *
from Capteur_de_distance import *

class Simulation :
    def __init__ (self, robotDonne) :
        """
        """
        self.mur_x = range(10) 
        self.mur_y = range(10)
        self.robot = robotDonne
        self.obs1 = Obstacle(6,2,2)
        self.obs2 = Obstacle(3,4,7)

    def simulationsansInterface(self):
        i=1
        t=2
        while(i<=t):
            #faire avancer le robot
	    self.robot.avancer(i,i)
            #methode d'evitement
            i+=0.1
            sleep(0.5)

    





