#!/usr/bin/python
# -*- coding: latin-1 -*-
from math import pi,sqrt
class Capteur_de_distance :
    def __init__(self, distanceCaptable) :
       self.distanceCaptable=distanceCaptable
    
    def distance(self,robot,obstacle):
        """
        Fonction prenant en paramètre le robot et l'obstacle afin de calculer leur distance et la retourner.
        """
        xr = robot.pos_x
        yr = robot.pos_y
        xo = obstacle.x
        yo = obstacle.y
        return sqrt((xo-xr)**2+(yo-yr)**2)
        
      
