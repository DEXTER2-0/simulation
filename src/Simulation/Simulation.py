from Robot import *
from Obstacle import *
from Roue import *
from Capteur_de_distance import *
import numpy as np

class Simulation :
    def __init__ (self, robotDonne, terrain, duree_boucle) :
        """
        """
        #self.mur_x = range(10) 
        #self.mur_y = range(10)
        self.robot = robotDonne
        self.terrain = terrain
        self.duree_boucle = duree_boucle
        #self.obs1 = Obstacle(6,2,2)
        #self.obs2 = Obstacle(3,4,7)
        
    
    def collision(self):
    for i in self.terrain.liste_obstacles:
        d=np.sqrt((self.ia.robot.x-i.x)**2+(self.ia.robot.y-i.y)**2)
        if(d<=(self.ia.robot.rayon+i.rayon)): # collision de deux cercles
            self.ia.robot.arreter_urgence()
        elif (d<=(self.ia.robot.rayon)): # collision d'un cercle et d'un rectangle A COMPLETER
            self.ia.robot.arret_urgence()
    
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

    





