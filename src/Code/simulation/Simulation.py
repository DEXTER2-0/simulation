from Code.simulation import constantes as cs
from Code.simulation import Vecteur as vect
import time as time #pour pouvoir controler le temps de la boucle while True
from datetime import datetime
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
        self.t_1=datetime.now()

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
      t0=datetime.now()
      dt=(t0-self.t_1).total_seconds()
      self.t_1=t0
      if self.collision() :
          print("COOOOLISIONNNNN ")
          self.stop()
          return 
      if self.robot.roue_gauche.vDegParSec==0 and self.robot.roue_gauche.vDegParSec==0 : # a l'arret
          return
      if self.robot.roue_gauche.vDegParSec==self.robot.roue_gauche.vDegParSec : # ligne droite
          angle=dt*self.robot.roue_gauche.vDegParSec
          self.robot.pos_roue_g+=angle
          self.robot.pos_roue_d+=angle
          k,r=divmod(angle,360)
          distance=k*cs.CIRCONFERENCE_ROUES+(r*cs.CIRCONFERENCE_ROUES)/360
          self.robot.centre+=(self.robot.vec*distance).pointer_vers()
          self.robot.update()
          return
      if self.robot.roue_droite.vDegParSec==0 and self.robot.roue_gauche.vDegParSec!=0 : # tourne avec seulement la roue gauche
          mil=vect.Point.milieu(self.robot.cote_bas_gauche,self.robot.cote_bas_droit)
          angle=dt*self.robot.roue_gauche.vDegParSec
          self.robot.pos_roue_g+=angle
          k,r=divmod(angle,360)
          distance=k*cs.CIRCONFERENCE_ROUES+(r*cs.CIRCONFERENCE_ROUES)/360
          angle=distance*180/(pi*cs.DIAMETRE_ROUES)
          angle=-angle
      if self.robot.roue_gauche.vDegParSec==0 and self.robot.roue_droite.vDegParSec!=0 : # tourner avec seulement la roue droite
          mil=vect.Point.milieu(self.robot.cote_bas_gauche,self.robot.cote_bas_droite)
          angle=dt*self.robot.roue_droite.vDegParSec
          self.robot.pos_roue_d+=angle
          k,r=divmod(angle,360)
          distance=k*cs.CIRCONFERENCE_ROUES+(r*cs.CIRCONFERENCE_ROUES)/360
          angle=distance*180/(pi*cs.DIAMETRE_ROUES)
      self.angle_fait+=angle
      self.robot.vec=vect.Vecteur.get_vect_from_angle(self.angle_fait)
      self.robot.centre.rotation(mil,angle)
      self.robot.update()
