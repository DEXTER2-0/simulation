from Modele import Robot
from Modele import Roue  
from Modele import constantes
from Modele import Obstacle
from Controleur import IA
from Modele import Terrain
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
        for i in self.terrain.liste_obstacles:
            d=np.sqrt((self.ia.robot.x-i.x)**2+(self.ia.robot.y-i.y)**2)
            if(d<=(self.ia.robot.rayon+i.rayon)): # collision de deux cercles
                self.ia.robot.arreter_urgence()
            elif (d<=(self.ia.robot.rayon)): # collision d'un cercle et d'un rectangle A COMPLETER
                self.ia.robot.arret_urgence()
    
    def update_simulation(self):
        distance = self.robot.capteurDistance.senseur_de_distance(self.ia.pos_x, self.ia.pos_y, self.ia.angle, 0.5, self.terrain.liste_obstacle)
        if distance > 1 :
            self.ia.bouger(150,150)
            self.ia.nouvelle_position2(self.duree_boucle)
            time.sleep(1)
            print(self.ia)
        else :
            print("obstacle à ",distance ,"metre ARRET !!")
    

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

    





