from Robot import *
from Obstacle import *
from Roue import *
from Capteur_de_distance import *

class IA :
    def __init__ (self, robot,r=0,angle = 0, pos_x = 0, pos_y = 0) :
        """
        """
        self.r=r
        self.angle = angle
        #self.vitesse_er 
        #self.vitesse_et
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.robot = robot