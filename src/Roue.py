#!/usr/bin/python
# -*- coding: latin-1 -*-
from math import pi

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
	
