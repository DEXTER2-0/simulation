from Robot import * # Permet d'utiliser la classe Robot se trouvant dans le meme repertoire
from Roue import * # Permet d'utiliser la classe Roue se trouvant dans le meme repertoire
import time #pour pouvoir controler le temps de la boucle while True
from math import *
from IA import *
from Obstacle import *


# Initialisation des constantes du robot
RAYON_DES_ROUES_CM = 1 # ---->  r
VITESSE_MAX_TOUR_PAR_SEC = 30 #pas encore utilisé
RAYON_ROBOT_CM = 1
DISTANCE_ROUE_CENTRE_CM = 100 # ----->  l

#Initialisation du Robot
robot = Robot(RAYON_DES_ROUES_CM, RAYON_ROBOT_CM, 8,VITESSE_MAX_TOUR_PAR_SEC)

#Initialisation d'un obstacle en (5,0) de rayon 2
obstacle = Obstacle(2,5,0)

#Initilaisation de l'IA
ia = IA(robot)

# Les coordonnées (Permet de placer le robot au milieu de la fenetre)
#ia.pos_x = 800/2
ia.pos_x=1
ia.pos_y=1
#ia.pos_y = 800/2

while True :
	# Si le capteur detecte un obstacle a 1.5  metre
	#if robot.capteurDistance.distance(ia.pos_x,ia.pos_y,obstacle) < 1.5 :
	ia.bouger(150,150)
	ia.nouvelle_position2(1)
	time.sleep(1)
	print(ia)
	print(ia.robot.roue_droite.vTourParSec)
	print(ia.robot.roue_gauche.vTourParSec)
	#else :
	#	ia.evite()
	#	ia.nouvelle_position2(1)
	#	time.sleep(1)
	#	print(ia)
	#	print(ia.robot.roue_droite.vTourParSec)
	#	print(ia.robot.roue_gauche.vTourParSec)
