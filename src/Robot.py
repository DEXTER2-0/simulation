#!/usr/bin/python
# -*- coding: latin-1 -*-
from Roue import * # Permet d'utiliser la classe Roue se trouvant dans le meme repertoire
from Capteur_de_distance import * # Permet d'utiliser la classe Capteur_de_distance se trouvant dans le meme repertoire
import math
import numpy as np
class Robot :
	def __init__ (self, rayonRouesCm,rayonDuRobotCm, capteur,vMaxTourParSec, pos_x = 0, pos_y = 0) :
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
		self.pos_x = pos_x
		self.pos_y = pos_y

	def est_entrain_de_rouler(self) :
		"""
		Fonction testant la vitesse des roues afin de retourner un booléen corresponsant à si le robot roule ou non
		"""
		if self.roue_droite.vTourParSec==0 and self.roue_gauche.vTourParSec==0 :
			return False
		else :
			return True

	def avancer(self,vitesseVoulue_kmh_er,vitesseVoulue_kmh_et) :
		"""
		Fonction prenant en paramètre la vitesse voulue en km/h projetée sur l'axe er et la vitesse voulue en km/h projetée sur l'axe et
		puis vérifiant que les vitesses permettent d'avancer (>0) afin de calculer la vitesse voulue en km/h
		et de la transmettre aux roues
		"""
		assert(vitesseVoulue_kmh_er > 0)
		assert(vitesseVoulue_kmh_et > 0)
		self.vitesse_er=vitesseVoulue_kmh_er
		self.vitesse_et=vitesseVoulue_kmh_et
		vitesseVoulue_kmh=np.sqrt(vitesseVoulue_kmh_er**2+vitesseVoulue_kmh_et**2)
		self.accelerer(vitesseVoulue_kmh)
		#print("le robot avance à une vitesse ", vitesseVoulue_kmh)

	def reculer(self,vitesseVoulue_kmh_er,vitesseVoulue_kmh_et) :
		"""
		Fonction prenant en paramètre la vitesse voulue en km/h projetée sur l'axe er et la vitesse voulue en km/h projetée sur l'axe et
		puis vérifiant que les vitesses permettent d'avancer (<0) afin de calculer la vitesse voulue en km/h
		et de la transmettre aux roues
		"""
		assert(vitesseVoulue_kmh_er < 0)
		assert(vitesseVoulue_kmh_et < 0)
		self.vitesse_er=vitesseVoulue_kmh_er
		self.vitesse_et=vitesseVoulue_kmh_et
		vitesseVoulue_kmh=-(np.sqrt(vitesseVoulue_kmh_er**2+vitesseVoulue_kmh_et**2))
		self.accelerer(vitesseVoulue_kmh)
		#print("le robot recule à une vitesse de ",vitesseVoulue_kmh)


	def arreter_urgence(self):
		"""
		Fonction arretant le robot en mettant la vitesses des roues à 0 d'un coup
		"""
		self.roue_gauche.setVitesse(0)
		self.roue_droite.setVitesse(0)
		#print("le robot est en arret")

	def tourner(self,angleEnRad,tempsDonneEnSec):
		"""
		Fonction prenant en paramètre l'angle en rad que le robot doit effectuer et le temps qu'il a pour faire cette rotation
		commençant par arrêter le robot puis calculant la vitesse angulaire et la vitesse en km/h de cette rotation
		avant de tester si l'angle est positif, dans ce cas la vitesse est transmise à la roue gauche pour tourner à droite, 
		ou négatif, dans ce cas la vitesse est transmise à la roue droite pour tourner à gauche
		"""
		self.arreter_urgence()
		vitesseAng = angleEnRad/tempsDonneEnSec
		vitessekmh = 3.6*self.roue_droite.taille_cm*(10**(-2))*vitesseAng
		if(angleEnRad<0):
			self.roue_droite.setVitesse(vitessekmh)
			self.roue_gauche.setVitesse(0)
	#	print("le robot tourne vers la gauche d'un angle de : ", angleEnRad)
		if(angleEnRad>0):
			self.roue_droite.setVitesse(0)
			self.roue_gauche.setVitesse(vitessekmh)
	#	print("le robot tourne vers la droite d'un angle de :  " ,angleEnRad)

	def accelerer(self,vitesseVoule):
		"""
		Fonction prenant en paramètre la vitesse à atteindre en km/h
		puis transmets des vitesses aux roues par pas de 0,1 km/h tant que la vitesse voulue n'est pas atteinte
		"""

	#	assert(self.roue_gauche.vTourParSec==self.roue_droite.vTourParSec)
		assert(self.roue_gauche.vTourParSec != 0)
		assert(self.roue_gauche.vTourParSec==self.roue_gauche.vTourParSec)
<<<<<<< HEAD
	#	print(self.roue_gauche.vTourParSec)

		vitesse_actuelle=(36*np.pi*self.roue_gauche.taille_cm)/(5*self.roue_gauche.vTourParSec)
=======
		print(self.roue_gauche.vTourParSec)
		if (self.roue_gauche.vTourParSec > 0) :
			vitesse_actuelle=(36*np.pi*self.roue_gauche.taille_cm)/(5*self.roue_gauche.vTourParSec)
		else :
			vitesse_actuelle = 0
>>>>>>> 3fb04e685be9380960781b7705d142d51b962b6f
		while(vitesse_actuelle <= vitesseVoule):
				self.roue_gauche.setVitesse(vitesse_actuelle+1)
				self.roue_gauche.setVitesse(vitesse_actuelle+1)
				vitesse_actuelle=(36*np.pi*self.roue_gauche.taille_cm)/(5*self.roue_gauche.vTourParSec)

	#	print("le robot roule à la vitesse voulue apres acceleration :  " , vitesse_actuelle)

	def decelerer(self,vitesseVoule):
		"""
		Fonction prenant en paramètre la vitesse à atteindre en km/h
		puis transmets des vitesses aux roues par pas de 0,1 km/h tant que la vitesse voulue n'est pas atteinte
		"""
		assert(self.roue_gauche.vTourParSec>0)
		vitesse_actuelle=(36*np.pi*self.roue_gauche.taille_cm)/(5*self.roue_gauche.vTourParSec)
		while(vitesse_actuelle >= vitesseVoule):
			self.roue_gauche.setVitesse(vitesse_actuelle-1)
			self.roue_gauche.setVitesse(vitesse_actuelle-1)
			vitesse_actuelle=(36*np.pi*self.roue_gauche.taille_cm)/(5*self.roue_gauche.vTourParSec)



	#	print("le robot roule à la vitesse voulue apres deceleration : ", vitesse_actuelle)


	def arreter(self):
		"""
		Fonction arretant le robot par décélération jusqu'à l'arrêt
		"""
		self.decelerer(0)
	#	print("le robot s'arrete")

	def conversion_polaire_vers_cartesienne(self):
		"""
		Fonction faisant la conversion des coordonnées polaires en coordonées cartésiennes
		formules utilisées : x=r*cos(theta) et y=r*sin(theta)
		"""
		pos_x = self.r * np.cos(self.angle)
		pos_y = self.r * np.sin(self.angle)
		return pos_x, pos_y

	def conversion_cartesienne_vers_polaire(self):
		"""
		Fonction faisant la conversion des coordonnées cartésiennes en coordonées polaires
		formules utilisées : r=(x²+y²)^(1/2) et theta=arctan(y/x)
		"""
		r = np.sqrt(self.pos_x**2 + self.pos_y**2)
		angle= np.arctan(self.pos_y/self.pos_x)
		return r, angle

	def nouvelle_position(self,duree):
		"""
		Fonction prenant en paramètre la durée en s depuis le calcul de la dernière position
		puis calcul le nouveau r et le nouvel angle
		formules utilisées : r+=vitesse projetée sur l'axe er*t et theta+=vitesse projetée sur l'axe et*t/r
		"""
		self.r+=self.vitesse_er*duree
		self.angle+=self.vitesse_et*duree/self.r
		val = self.conversion_polaire_vers_cartesienne()
		self.pos_x = val[0]
		self.pos_y = val[1]

	def evite_obstacles(self,Obstacle):
		"""
		Fonction prenant en paramètre l'obstacle et si la distance captée par le capteur entre le robot et l'obstacle est 
		inférieure à 10 cm, alors le robot effectue une rotation d'un quart de tour vers la gauche
		"""
		val=np.pi/2
		if(self.capteurDistance.distance(self,Obstacle) < 10):
			self.tourner(val,1)
	#		print("le robot a évité l'obstacle")
		else :
	#		print("pas de danger , no worries")


        def __str__ (self) :

		"""
		Fonction de redéfinition de la methode print(monInstance)
		"""
		res = "Le robot en position (" + str(self.pos_x) +","+ str(self.pos_y) + ")"
		# Le test suivant permet de faire un affichage du robot selon s'il roule ou pas#
		if (self.est_entrain_de_rouler()) :
			res += "est en train de rouler"
		else :
			res += " est à l'arret"
		return res



