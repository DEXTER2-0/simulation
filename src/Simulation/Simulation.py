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
    
    
    
    def simul(self):
    i=0
    t=
    self.ia.robot.bouger(vr,vl)
    while (i<t):
        for i in self.terrain.liste_obstacle:
            self.ia.robot.eviter(i)
        self.collision()
        i+=0.1
    self.robot.arret()

    





