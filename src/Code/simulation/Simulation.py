from Code.simulation import constantes as cs
import time as time #pour pouvoir controler le temps de la boucle while True
import numpy as np
from math import *
from threading import Thread

class Simulation(Thread) : 
    def __init__ (self, robot,terrain,fps) :
        """     
	    :param robot : Robot utilise
	    :param terrain : Terrain utilise
	    :param dt : duree de simulation
        """
        super(Simulation, self).__init__()
        self.robot = robot
        self.terrain = terrain
        self.fps = fps
        self.capteurOn = False
        self.encours= True
        self.t_1=time.datetime.now()

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

    def run(self):
      """
      le step de la simulation
      """
      while self.encours:   #tant qu'on run 
        self.update() #on met a jour la simulation 
        time.sleep(1/self.fps)
		
    def stop(self):
        self.encours = False
            
    def update(self):
      """
      met a jour la simulation selon le temps ecoule
      """
      t0=time.datetime.now()
      dt=(t0-self.t_1).total_seconds()
      self.t_1=t0
      if self.robot.roue_gauche.vDegParSec==0 and self.robot.roue_gauche.vDegParSec==0 :
          return
      if self.robot.roue_gauche.vDegParSec==self.robot.roue_gauche.vDegParSec :
          angle=dt*self.robot.roue_gauche.vDegParSec
          self.robot.pos_roue_g+=angle
          self.robot.pos_roue_d+=angle
          k,r=divmod(angle,360)
          distance=k*cs.CIRCONFERENCE_ROUES+(r*cs.CIRCONFERENCE_ROUES)/360
          self.robot.centre+=(self.robot.vec*distance).pointer_vers()
          return
      if self.collision() :
          print("COOOOLISIONNNNN ")
          self.stop()
          return 
      else :
          self.get_pos(self.robot)
