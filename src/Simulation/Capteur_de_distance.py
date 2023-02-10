#!/usr/bin/python
# -*- coding: latin-1 -*-
from math import pi,sqrt,sin,cos
class Capteur_de_distance :
    def __init__(self, distanceCaptable) :
       """
       Fonction d'initialisation prenant en paramètre la distance maximale captable possible
       """
       self.distanceCaptable=distanceCaptable
    
    
    def distance(self,x,y,obstacle):
        """
        Fonction prenant en paramètre le robot et l'obstacle afin de calculer leur distance 
        (racine carrée des carré des différences entre les positions selon x et selon y) et la retourner.
        """
        xr = x
        yr = y
        xo = obstacle.x
        yo = obstacle.y
        return sqrt((xo-xr)**2+(yo-yr)**2)

    def senseur_de_distance(self,ia_pos_x,ia_pos_y,angle_robot,distanceCaptable,le_pas,l_obstacle):
        """
        Suppose que la liste d'obstacle sont des cercles
        l_obstacle est une liste d'obstacle
        Aide page 16 du td2
        """
        k=0
        x = ia_pos_x
        y = ia_pos_y
        while k*le_pas < distanceCaptable :
            x = ia_pos_x + le_pas*cos(angle_robot)
            y = ia_pos_y + le_pas*sin(angle_robot)
            for i in range(len(l_obstacle)) :
                obstacle = l_obstacle[i]
                if (sqrt((obstacle.x-x)**2+(obstacle.y-y)**2)) < obstacle.rayon:
                    return sqrt((x-ia_pos_x)**2+(y-ia_pos_y)**2)

        return distanceCaptable



      
