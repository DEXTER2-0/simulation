#!/usr/bin/python
# -*- coding: latin-1 -*-
from Modele import Roue 
from Modele import Capteur_de_distance 
import math
import numpy as np

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

