#import Robot
#import Obstacle
#import IA as ia
from TestScript import constantes as cs
#import Terrain
import time #pour pouvoir controler le temps de la boucle while True
import numpy as np
from math import *
import logging



class Simulation : 
    def __init__ (self, ia, robot,terrain,duree_boucle,pos_x=0,pos_y=0,r=0,angle=0) :
	    
        """
        """
        #self.mur_x = range(10) 
        #self.mur_y = range(10)
        self.ia = ia
        self.robot = robot
        self.terrain = terrain
        self.duree_boucle = duree_boucle
        self.pos_x=pos_x
        self.pos_y=pos_y
        self.r=r
        self.angle = angle
    
	
        #self.obs1 = Obstacle(6,2,2)
        #self.obs2 = Obstacle(3,4,7)
        
    
    def collision(self):
        """
        Suppose objet est cercle
        """
        for obstacle in self.terrain.liste_obstacle: #pour chaque obstacle
            d=np.sqrt((self.pos_x-obstacle.x)**2+(self.pos_y-obstacle.y)**2) #distance euclidienne entre le robot et l'obstacle
            if(d<=(self.ia.robot.rayonDuRobotCm+obstacle.longueur)): # collision de deux cercles
                self.ia.robot.arreter_urgence()
                logging.debug("Collision détectée : arret d'urgence")
            #elif (d<=(self.ia.robot.rayon)): # collision d'un cercle et d'un rectangle A COMPLETER
             #   self.ia.robot.arret_urgence()
	
    def nouvelle_position2(self,duree):
        """
        Doit etre appelé apres la methode bouger() pour pouvoir mettre a jours les 
        oordonées du robot ainsi que son angle d'orientation					                      
        """
        self.pos_x = self.pos_x + self.ia.v * cos(self.angle)*duree
        self.pos_y = self.pos_y + self.ia.v * sin(self.angle)*duree
        self.angle = self.angle + self.ia.w * duree
    
    def evite_murs(self):
        if (self.pos_x>=(cs.WIDTH/2)-2) or (self.pos_x<=-(cs.WIDTH/2)+2) or (self.pos_y>=(cs.HEIGHT/2)-2) or (self.pos_y<=-(cs.HEIGHT/2)+2):
            self.ia.bouger(0,(pi*self.robot.l*0.01)/(2*self.robot.roue_droite.taille_cm*0.01))
		
    def update_simulation(self):
        distance = self.robot.capteurDistance.senseur_de_distance(self.pos_x, self.pos_y, self.angle, 0.5, self.terrain.liste_obstacle)
        self.collision()
        logging.debug(f"{distance}")
        if distance > cs.DISTANCE_MIN_ARRET:
            self.ia.bouger(cs.V_ANGULAIRE_G,cs.V_ANGULAIRE_D)
            self.nouvelle_position2(self.duree_boucle)
            time.sleep(0.001)
            logging.debug(f"{self.pos_x},{self.pos_y}")
        else :  
            logging.debug(f"{self.pos_x},{self.pos_y}")
            self.ia.evite()
            #self.nouvelle_position2(self.duree_boucle)
        

    

    #def simul(self):
    #    i=0
    #    t=
    #    self.ia.robot.bouger(vr,vl)
    #    while (i<t):
    #        for i in self.terrain.liste_obstacle:
    #            self.ia.robot.eviter(i)
    #        self.collision()
    #        i+=0.1
    #self.robot.arret()

    





