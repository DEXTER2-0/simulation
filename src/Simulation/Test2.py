from Robot import * # Permet d'utiliser la classe Robot se trouvant dans le meme repertoire
from Roue import * # Permet d'utiliser la classe Roue se trouvant dans le meme repertoire
import time #pour pouvoir controler le temps de la boucle while True
from math import *
from IA import *


# Initialisation des constantes du robot
RAYON_DES_ROUES_CM = 1 # ---->  r
VITESSE_MAX_TOUR_PAR_SEC = 30 #pas encore utilisé
RAYON_ROBOT_CM = 1
DISTANCE_ROUE_CENTRE_CM = 100 # ----->  l

#Initialisation du Robot
robot = Robot(RAYON_DES_ROUES_CM, RAYON_ROBOT_CM, 10,VITESSE_MAX_TOUR_PAR_SEC)


#Initilaisation de l'IA
ia = IA(robot)

# Les coordonnées (Permet de placer le robot au milieu de la fenetre)
#ia.pos_x = 800/2
#ia.pos_y = 800/2

while True :
	ia.tourner2(200.1,0)
	ia.nouvelle_position2(1)
	time.sleep(1)
	print(ia)