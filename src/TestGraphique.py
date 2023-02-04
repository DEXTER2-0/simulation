from Robot import * # Permet d'utiliser la classe Robot se trouvant dans le meme repertoire
from Roue import * # Permet d'utiliser la classe Roue se trouvant dans le meme repertoire
import time #pour pouvoir controler le temps de la boucle while True
from math import *

##----- Importation des Modules -----##
from tkinter import * 

def ang(T_en_sec): # calcul vitesse angulaire
    return (2*pi/T_en_sec)*RAYON_DES_ROUES_CM*0.01

# instanciation d'un robot, prenant en parametre les deux roue créer précédemment
robot = Robot(RAYON_DES_ROUES_CM, VITESSE_MAX_TOUR_PAR_SEC, RAYON_ROBOT_CM)

print(robot)


while True :
    robot.tourner2(3.14,0)
    robot.nouvelle_position2(1)
    time.sleep(5)
    print(robot)
