from Code.simulation import constantes as cs
import time as time #pour pouvoir controler le temps de la boucle while True
import numpy as np
from math import *
from threading import Thread

class Simulation(Thread) : 
    def __init__ (self, robot,terrain,dt) :
      """     
	:param robot : Robot utilise
	:param terrain : Terrain utilise
	:param dt : duree de simulation
   """
      super(Simulation, self).__init__()
      self.robot = robot
      self.terrain = terrain
      self.dt = dt
      self.capteurOn = False

    def collision(self): #PROBLEME x et y dans robot donc plus de self.pos_x
        """
        on suppose que tout objet est un cercle
        """
        if(self.robot == None):
              return False
        if (self.pos_x<=self.terrain.WIDTH_MIN) or (self.pos_y<=self.terrain.HEIGHT_MIN) or (self.pos_x>=self.terrain.WIDTH_MAX) or (self.pos_y>=self.terrain.HEIGHT_MAX):
            return True
        for obstacle in self.terrain.liste_obstacle: #pour chaque obstacle
            d=np.sqrt((self.pos_x-obstacle.x)**2+(self.pos_y-obstacle.y)**2) #distance euclidienne entre le robot et l'obstacle
            if(d<=(self.robot.rayonDuRobotCm+obstacle.longueur)): # collision de deux cercles
                return True
            #elif (d<=(self.ia.robot.rayon)): # collision d'un cercle et d'un rectangle A COMPLETER
             #   self.ia.robot.arret_urgence()
        return False

    def get_pos(self,robot):
        return robot.calcul_x(),robot.calcul_y()

    def run(self):
      """
      le step de la simulation
      """
      self.encours= True
      while self.encours:   #tant qu'on run 
         self._lastTime = time.time()    # on sauvegarde l'instant du run 
         time.sleep(self.dt)     #on fait un sleep de dt afin de calculer l'intervalle de temps 
         self._ITemps = time.time() - self._lastTime   #on calcule l'intervalle de temps 
         self.update() #on met a jour la simulation 
		
    def stop(self):
        self.encours = False
            
    def update(self):
      """
      met a jour la simulation selon le temps ecoule
      """
      if self.collision() :
          print("COOOOLISIONNNNN ")
          self.stop()
          return 
      else :
          self.get_pos(self.robot)
