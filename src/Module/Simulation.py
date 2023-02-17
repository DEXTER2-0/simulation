#import Robot
#import Obstacle
#import IA as ia
from TestScript import constantes as cs
#import Terrain
import time #pour pouvoir controler le temps de la boucle while True
import numpy as np



class Simulation : 
    def __init__ (self, ia, robot, terrain, duree_boucle) :
        """
        """
        #self.mur_x = range(10) 
        #self.mur_y = range(10)
        self.ia = ia
        self.robot = robot
        self.terrain = terrain
        self.duree_boucle = duree_boucle
        #self.obs1 = Obstacle(6,2,2)
        #self.obs2 = Obstacle(3,4,7)
        
    
    def collision(self):
        """
        Suppose objet est cercle
        """
        for obstacle in self.terrain.liste_obstacle: #pour chaque obstacle
            d=np.sqrt((self.ia.pos_x-obstacle.x)**2+(self.ia.pos_y-obstacle.y)**2) #distance euclidienne entre le robot et l'obstacle
            if(d<=(self.ia.robot.rayonDuRobotCm+obstacle.longueur)): # collision de deux cercles
                self.ia.robot.arreter_urgence()
                print("Collision détectée : arret d'urgence")
            #elif (d<=(self.ia.robot.rayon)): # collision d'un cercle et d'un rectangle A COMPLETER
             #   self.ia.robot.arret_urgence()
	    
    
    def update_simulation(self):
        print("APPEELLL UPPDDAAAATTEEE  ")
        distance = self.robot.capteurDistance.senseur_de_distance(self.ia.pos_x, self.ia.pos_y, self.ia.angle, 0.5, self.terrain.liste_obstacle)
        self.collision()
        print(distance)
        if distance > cs.DISTANCE_MIN_ARRET:
            self.ia.bouger(cs.V_ANGULAIRE_G,cs.V_ANGULAIRE_D)
            self.ia.nouvelle_position2(self.duree_boucle)
            time.sleep(0.001)
            print(self.ia)
        else :  
            #self.ia.evite()
            self.ia.bouger(cs.V_ANGULAIRE_G,cs.V_ANGULAIRE_D)
            self.ia.nouvelle_position2(self.duree_boucle)
            #angle_depart = self.ia.angle
            #print(self.ia)

            #while self.ia.angle <= angle_depart - (np.pi/2) : 
            #    self.ia.evite()
            #print("obstacle à ",distance ,"mettre ARRET !!")

    

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

    





