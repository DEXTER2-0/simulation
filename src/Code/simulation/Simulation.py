#import Robot
from Code.simulation import constantes as cs
#import Terrain
import time as time#pour pouvoir controler le temps de la boucle while True
import numpy as np
from math import *
import logging
from threading import Thread
#logging.basicConfig(filename='Simulation.log', filemode='w', level=logging.DEBUG)



class Simulation(Thread) : 
    def __init__ (self, robot,terrain,dt,pos_x=0,pos_y=0,r=0,angle=0) :
        """     
	:param robot : Robot utilisé
	:param terrain : Terrain utilisé
	:param duree_boucle : duree de simulation
    """
        #self.mur_x = range(10) 
        #self.mur_y = range(10)

        super(Simulation, self).__init__()
        self.robot = robot
        self.terrain = terrain
        self.dt = dt
        self.pos_x=pos_x
        self.pos_y=pos_y
        self.r=r
        self.angle = angle
	

	    #partie capteur de distance :
	    self.capteurOn = False
	      #coordonnées du dernier point capté par le capteur de distance 
    
	    self.lastX = 0  
	    self.lastY=0


    
	
        #self.obs1 = Obstacle(6,2,2)
        #self.obs2 = Obstacle(3,4,7)
    



    def capterDistance(self,robot):
	    Distance=0
	    Vect0=(cos(angle))
	    Vect1=sin(-angle)
	    RayonCoord=(pos_x + Vect0 * robot.rayonDuRobotCm,pos_y + Vect1 * robot.rayonDuRobotCm)

	    for i in range(0,len(self.terrain.getListeObstacles())):
		    if self.terrain.getObstacle(i).Capte(RayonCoord[0] , RayonCoord[1]):
			    self.SensorOn= True
			    self.newPos_x = RayonCoord[0]	




   def collision(self):
        """
        Suppose objet est cercle
        """
        if(self.robot == None):
              return 0
        if (self.pos_x<=0) or (self.pos_y<=0) or (self.pos_x>=cs.WIDTH) or (self.pos_y>=cs.HEIGHT):
            logging.debug("Collision détectée : arret d'urgence")
            return 1
        for obstacle in self.terrain.liste_obstacle: #pour chaque obstacle
            d=np.sqrt((self.pos_x-obstacle.x)**2+(self.pos_y-obstacle.y)**2) #distance euclidienne entre le robot et l'obstacle
            if(d<=(self.robot.rayonDuRobotCm+obstacle.longueur)): # collision de deux cercles
                logging.debug("Collision détectée : arret d'urgence")
                return 1
            #elif (d<=(self.ia.robot.rayon)): # collision d'un cercle et d'un rectangle A COMPLETER
             #   self.ia.robot.arret_urgence()
        return 0





    def nouvelle_position2(self,duree):
        """
	:param duree : duree passee depuis le dernier calcul de la position
        Doit etre appelé apres la methode bouger() pour pouvoir mettre a jours les 
        oordonées du robot ainsi que son angle d'orientation					                      
        """

        self.pos_x = self.pos_x + self.robot.v * cos(self.angle)*duree
        self.pos_y = self.pos_y + self.robot.v * sin(self.angle)*duree
        self.angle = self.angle + self.robot.new_orientation * duree


	
    def step(self):
	    "le step de la simulation "
        self.step = True
        while self.step:   #tant qu'on run 
	        self._lastTime = time.time()    # on sauvegarde l'instant du run 
		    time.sleep(self._dt)     #on fait un sleep de dt afin de calculer l'intervalle de temps 
	        self._ITemps = time.time() - self._lastTime   #on calcule l'intervalle de temps 
		    self.update() #on met à jour la simulation 
		
    def stop(self): 
	    self.stop = False

    def update(self):
	    """ met à jour la simulation selon le temps écoulé """
	    if self.collision() == 1 :
	        self.robot=None
	    if self.collision() == 0:
	    	self.nouvelle_position2(self.dt)
		


