#!/usr/bin/python
# -*- coding: latin-1 -*-
from Modele import Roue as r
from Modele import Capteur_de_distance as cdd
from math import pi
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
		self.roue_gauche = r.Roue(rayonRouesCm, vMaxTourParSec)
		self.roue_droite = r.Roue(rayonRouesCm, vMaxTourParSec)
		self.capteurDistance = cdd.Capteur_de_distance(capteur)
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
	
