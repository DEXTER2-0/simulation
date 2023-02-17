#!/usr/bin/python
# -*- coding: latin-1 -*-

from TestScript import constantes as cs
from math import pi,sqrt,sin,cos

class Robot :
	def __init__ (self, rayonRouesCm,rayonDuRobotCm, capteur,vMaxTourParSec,l=1) :
		"""
		Fonction d'initialisation prenant en paramètre le rayon des roues en cm, le rayon du robot en cm,
		la distance maximale captable par le capteur de distance, la vitesse maximale possible pour les roues,
		les coordonnées polaires et les coordonnées cartésiennes du robot
		Cette fonction instancie deux roues de la même taille et de même vitesse maximale, ainsi qu'un capteur de position
		"""
		assert(rayonRouesCm > 0)# Ne peut pas avoir un rayon < 0
		assert(vMaxTourParSec > 0) # Ne peut pavoir une vitesse max < 0
		assert(rayonDuRobotCm > 0) # Ne peut pas avoir un rayon < 0
		self.roue_gauche = Roue(rayonRouesCm, vMaxTourParSec)
		self.roue_droite = Roue(rayonRouesCm, vMaxTourParSec)
		self.capteurDistance = Capteur_de_distance(capteur)
		self.rayonDuRobotCm = rayonDuRobotCm
		#self.pos_x = pos_x
		#self.pos_y = pos_y
        #self.robot = robot
		#self.r=r
        #self.angle = angle
		# l = 2*rayon du robot
		self.l=l*2*rayonDuRobotCm	

####------------------------ ROUE --------------------------##

class Roue :
	def __init__ (self, taille_cm, vMaxTourParSec) :
		"""
		Fonction d'initialisation prenant en paramètre le rayon en cm et la vitesse maximale possible pour les roues
		"""
		self.taille_cm = taille_cm
		self.vMaxTourParSec = vMaxTourParSec
		self.vTourParSec = 0

	def __str__ (self) :
		"""
		Fonction de redéfinition de la methode print(monInstance)
		""" 
		res = "Roue de taille " + str(self.taille_cm) + " cm"
		if self.vTourParSec == 0: # Si la roue est à l'arret
			res += " est à l'arret" 

		else : # Si la roue tourne
			res += " roule à " + str(self.vTourParSec) + "tour/seconde"
		return res
	
	def setVitesse(self,vitesseVoulue_kmh) :
		"""
		Formule prenant en paramètre la vitesse voulue en km/h et calculant sa converion en vitesse de rotation n en tr/s et la retourne
		puis donnant évaluant si la vitesse demandée est possible et de donner soit cette vitesse soit la vitesse maximale aux roues
		formule de conversion utilisée : N=(5*v)/(36*pi*rayon_en_metre)
		"""
		#print("la vitesse de la roue était de:  ",self.vTourParSec)
		vVoulueTourParSec= (5*vitesseVoulue_kmh)/(36*pi*self.taille_cm*0.01)
		if (vVoulueTourParSec<=self.vMaxTourParSec):# Si la vitesse est possible pour la roue 
			self.vTourParSec=vVoulueTourParSec

		else : # Si la vitesse voulue est plus grande que la vitesse maximale possible
			self.vTourParSec=self.vMaxTourParSec
		#print("la nouvelle vitesse de la roue est de:  ",self.vTourParSec)

		return self.vTourParSec
	
####------------------------ Capteur_de_distance --------------------------##

from math import pi,sqrt,sin,cos
import logging

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

    def senseur_de_distance(self,ia_pos_x,ia_pos_y,angle_robot,le_pas,l_obstacle):
        """
        Aide page 16 du td2
        Suppose que la liste d'obstac le sont des cercles
        l_obstacle : est une liste d'obstacle
        ia.pos_y et ia.pos_y : permettent de récuperer les coordonnée actuelles du robot
        angle : permet au capteur de savoir dans quelle direction lancer le laser
        le_pas : permet de couper en plusieurs morceaux la distance avant de rencontrer un obstacle 
        """
        k=0
        x = ia_pos_x
        y = ia_pos_y
        #print("Distance Captable = ",self.distanceCaptable)
        while k*le_pas < self.distanceCaptable :
            x = x + cos(angle_robot) * le_pas #Lance le laser dans la bonne direction
            y = y + sin(angle_robot) * le_pas #Lance le laser dans la bonne direction
            logging.debug(f"capteur -> ({x},{y})") 
            # Verification si les coordonées du laser se trouve dans un obstacle(cercle)
            for i in range(len(l_obstacle)) :
                obstacle = l_obstacle[i]
                
                # Si a un moment le laser se trouve dans un obstacle
                if(self.distance(x,y,obstacle)) < obstacle.longueur + cs.RAYON_ROBOT_CM +5: #obstacle.longueur car dans obstacle attribut longueur m¨
                    logging.debug(f"obstacle à : {sqrt((x-ia_pos_x)**2+(y-ia_pos_y)**2)}")

                    return sqrt((x-ia_pos_x)**2+(y-ia_pos_y)**2)
            k +=1
        logging.debug("**** Rien à l'horizon ****")
        return self.distanceCaptable



      
