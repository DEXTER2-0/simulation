#import Robot
#import Obstacle
#import IA as ia
import constantes as cs
#import Terrain
import time #pour pouvoir controler le temps de la boucle while True
import numpy as np
from math import *
import logging
#logging.basicConfig(filename='Simulation.log', filemode='w', level=logging.DEBUG)




class Simulation : 
    def __init__ (self, IAEvite, robot,terrain,duree_boucle,pos_x=0,pos_y=0,r=0,angle=0) :
        """    
        :param ia : IA utilisé
	:param robot : Robot utilisé
	:param terrain : Terrain utilisé
	:param duree_boucle : duree de simulation
    """
        #self.mur_x = range(10) 
        #self.mur_y = range(10)
        self.IAEvite = IAEvite
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
<<<<<<< HEAD:src/Module/Simulation.py
	
=======
        if (self.pos_x<=0) or (self.pos_y<=0) or (self.pos_x>=cs.WIDTH) or (self.pos_y>=cs.HEIGHT):
            self.IAEvite.arreter_urgence()
            logging.debug("Collision détectée : arret d'urgence")
            return 1
>>>>>>> ebab939247fb65e44eec3bdba38b70accb309eeb:src/Dexter/Simulation.py
        for obstacle in self.terrain.liste_obstacle: #pour chaque obstacle
            d=np.sqrt((self.pos_x-obstacle.x)**2+(self.pos_y-obstacle.y)**2) #distance euclidienne entre le robot et l'obstacle
            if(d<=(self.IAEvite.robot.rayonDuRobotCm+obstacle.longueur)): # collision de deux cercles
                self.IAEvite.arreter_urgence()
                logging.debug("Collision détectée : arret d'urgence")
                return 1
            #elif (d<=(self.ia.robot.rayon)): # collision d'un cercle et d'un rectangle A COMPLETER
             #   self.ia.robot.arret_urgence()
	
    def nouvelle_position2(self,duree):
        """
	:param duree : duree passee depuis le dernier calcul de la position
        Doit etre appelé apres la methode bouger() pour pouvoir mettre a jours les 
        oordonées du robot ainsi que son angle d'orientation					                      
        """
        self.pos_x = self.pos_x + self.IAEvite.v * cos(self.angle)*duree
        self.pos_y = self.pos_y + self.IAEvite.v * sin(self.angle)*duree
        self.angle = self.angle + self.IAEvite.w * duree
    
    def evite_murs(self):
        if (self.pos_x>=(cs.WIDTH/2)-2) or (self.pos_x<=-(cs.WIDTH/2)+2) or (self.pos_y>=(cs.HEIGHT/2)-2) or (self.pos_y<=-(cs.HEIGHT/2)+2):
            self.IAevite.setVitesseRobot(0,(pi*self.robot.l*0.01)/(2*self.robot.roue_droite.taille_cm*0.01))
        self.IAEvite.evite()
		
    def update_simulation(self):
        logging.debug(f"robot pos_x= {self.pos_x},robot pos_y={self.pos_y}, angle {self.angle}")
        distance = self.robot.capteurDistance.senseur_de_distance(self.pos_x, self.pos_y, self.angle, 0.1, self.terrain.liste_obstacle)
        if self.collision() == 1:
            exit(-1)
        logging.debug(f"capteur renvoie --> {distance}")
        #cpt =0
       # mur=False

        #if (((self.pos_x>=cs.WIDTH-20) or (self.pos_x<=20) or (self.pos_y>=cs.HEIGHT-20) or (self.pos_y<=20) ) and not(mur)):
        #    self.IAEvite.evite()
        #    self.nouvelle_position2(self.duree_boucle)
        #    self.IAEvite.setVitesseRobot(cs.V_ANGULAIRE_G,cs.V_ANGULAIRE_D)
        #    self.nouvelle_position2(self.duree_boucle)
        #    mur=True
        #if(((self.pos_x>=cs.WIDTH-20) or (self.pos_x<=20) or (self.pos_y>=cs.HEIGHT-20) or (self.pos_y<=20) ) and mur):
        #    self.IAEvite.setVitesseRobot(cs.V_ANGULAIRE_G-50,cs.V_ANGULAIRE_D+50)
        #    self.nouvelle_position2(self.duree_boucle)
        #    print("if -> angle = ",self.angle)
            
        if distance >cs.DISTANCE_MIN_ARRET:
            logging.debug(f"{distance}")
            self.IAEvite.setVitesseRobot(cs.V_ANGULAIRE_G,cs.V_ANGULAIRE_D)
            self.nouvelle_position2(self.duree_boucle)
            print("if -> angle = ",self.angle)
            #time.sleep(0.001)
        else : 
            print("EVITE!!!!!") 
            print("else -> angle = ",self.angle)
            logging.debug(f"{distance}")
            logging.debug(f"{cs.DISTANCE_MIN_ARRET}")
            self.IAEvite.evite()
            self.nouvelle_position2(self.duree_boucle)
        

    

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

    





