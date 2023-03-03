#!/usr/bin/python
# -*- coding: latin-1 -*-
from simulation import constantes as cs
from math import pi,sqrt,sin,cos

class Robot :
	def __init__ (self, rayonRouesCm,rayonDuRobotCm, capteur,vMaxDegParSec,l=1) :
		"""
		:param rayonRouesCm : rayon des roues en cm
		:param rayonDuRobotCm : rayon du cercle dans lequel s'inscrit le robot en cm
		:param capteur : Capteur utilisé
		:param vMaxRadParSec : vitesse maximale possible pour les roues en rad/s
		Cette fonction instancie deux roues de la même taille et de même vitesse maximale, ainsi qu'un capteur de position
		"""
		assert(rayonRouesCm > 0)# Ne peut pas avoir un rayon < 0
		assert(vMaxDegParSec > 0) # Ne peut pavoir une vitesse max < 0
		assert(rayonDuRobotCm > 0) # Ne peut pas avoir un rayon < 0
		self.roue_gauche = Roue(rayonRouesCm, vMaxDegParSec)
		self.roue_droite = Roue(rayonRouesCm, vMaxDegParSec)
		self.capteurDistance = Capteur_de_distance(capteur)
		self.rayonDuRobotCm = rayonDuRobotCm
		#self.pos_x = pos_x
		#self.pos_y = pos_y
        #self.robot = robot
		#self.r=r
        #self.angle = angle
		# l = 2*rayon du robot
		self.l=l*2*rayonDuRobotCm	

	def setMotorDps(self, ANG_G, ANG_D):
		"""
		cette methode suppose que les deux roues possede le meme rayon
		ANG_G prend une vitesse angulaire pour la roue gauche
		ANG_D prend une vitesse angulaire pour la roue droite
		"""
		# vitesse moyenn du robot
		
		#Donne l'information aux roues de la vitesse en rad/s de la vitesse qu'elles doivent avoir
		self.roue_gauche.vDegParSec = ANG_G
		self.roue_droite.vDegParSec = ANG_D

		
####------------------------ ROUE --------------------------##

class Roue :
	def __init__ (self, taille_cm, vMaxRadParSec) :
		"""
		:param taille_cm : taille de la roue en cm
		:param vMaxTourParSec : vitesse maximale possible pour les roues en rad/s
		"""
		self.taille_cm = taille_cm
		self.vMaxRadParSec = vMaxRadParSec
		self.vRadParSec = 0

	def __str__ (self) :
		"""
		Fonction de redéfinition de la methode print(monInstance)
		""" 
		res = "Roue de taille " + str(self.taille_cm) + " cm"
		if self.vRadParSec == 0: # Si la roue est à l'arret
			res += " est à l'arret" 

		else : # Si la roue tourne
			res += " roule à " + str(self.vRadParSec) + "tour/seconde"
		return res
	
####------------------------ Capteur_de_distance --------------------------##

from math import pi,sqrt,sin,cos
import logging

class Capteur_de_distance :
    def __init__(self, distanceCaptable) :
       """
       :param distanceCaptable : distance maximale captable possible
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

    def senseur_de_distance(self,pos_x,pos_y,angle_robot,le_pas,l_obstacle):
        """
        Aide page 16 du td2
        Suppose que la liste d'obstac le sont des cercles
        l_obstacle : est une liste d'obstacle
        pos_y et pos_y : permettent de récuperer les coordonnée actuelles du robot
        angle : permet au capteur de savoir dans quelle direction lancer le laser
        le_pas : permet de couper en plusieurs morceaux la distance avant de rencontrer un obstacle 
        """
        k=0
        x = pos_x
        y = pos_y

        print("Distance Captable = ",self.distanceCaptable)
        while k*le_pas < self.distanceCaptable :
            x = x + cos(angle_robot) * le_pas #Lance le laser dans la bonne direction
            y = y + sin(angle_robot) * le_pas #Lance le laser dans la bonne direction
            logging.debug(f"capteur -> ({x},{y})") 
            # Verification si les coordonées du laser se trouve dans un obstacle(cercle)
            for i in range(len(l_obstacle)) :
                obstacle = l_obstacle[i]
                
                # Si a un moment le laser se trouve dans un obstacle
                if(self.distance(x,y,obstacle)) <= obstacle.longueur : #obstacle.longueur car dans obstacle attribut longueur m¨
                    logging.debug(f"obstacle à : {sqrt((x-pos_x)**2+(y-pos_y)**2)}")

                    return sqrt((x-pos_x)**2+(y-pos_y)**2)-cs.RAYON_ROBOT_CM
            k +=1
        logging.debug("**** Rien à l'horizon ****")
        return self.distanceCaptable-cs.RAYON_ROBOT_CM
	






      
