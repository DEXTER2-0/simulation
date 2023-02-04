from Robot import * # Permet d'utiliser la classe Robot se trouvant dans le meme repertoire
from Roue import * # Permet d'utiliser la classe Roue se trouvant dans le meme repertoire
import time #pour pouvoir controler le temps de la boucle while True
from math import *

def ang(T_en_sec): # calcul vitesse angulaire
    return (2*pi/T_en_sec)*RAYON_DES_ROUES_CM*0.01

##----- Importation des Modules -----##
from tkinter import * 

# Initialisation des constantes du robot
RAYON_DES_ROUES_CM = 1 # ---->  r
VITESSE_MAX_TOUR_PAR_SEC = 30 #pas encore utilisé
RAYON_ROBOT_CM = 10
DISTANCE_ROUE_CENTRE_CM = 5 # ----->  l


##----- Création de la fenetre -----##
fen = Tk() 
WIDTH = 600 # axe des x
HEIGHT = 600 # axe des y
canvas = Canvas(fen, width = WIDTH, height = HEIGHT, bg = 'yellow') #fentre graphique
canvas.pack(fill="both", expand=True)

# formule de la distance
def distance(xA, yA, xB, yB):
    return sqrt((xB-xA)**2 + (yB-yA)**2)

# Le robot à déplacer
robot = Robot(RAYON_DES_ROUES_CM, RAYON_ROBOT_CM, VITESSE_MAX_TOUR_PAR_SEC)


print(robot.rayonDuRobotCm)

# Les coordonnées (Permet de placer le robot au milieu de la fenetre)
robot.pos_x = WIDTH/2
robot.pos_y = HEIGHT/2

# Permet de représenter le robot sur tkinter
representation_robot = canvas.create_oval(robot.pos_x - robot.rayonDuRobotCm , robot.pos_y - robot.rayonDuRobotCm,robot.pos_x + robot.rayonDuRobotCm, robot.pos_y + robot.rayonDuRobotCm, width=2, fill="purple")

obstacle1 = canvas.create_oval(20, 20, 40, 40,width=2, fill="orange")
obstacle2 = canvas.create_oval(70, 5, 80, 15, width=2, fill="green")
obstacle3 = canvas.create_oval(480, 510, 510, 540, width=2, fill="pink")
obstacle4 = canvas.create_oval(300, 150, 315, 165, width=2, fill="brown")
obstacle5 = canvas.create_oval(150, 400, 200, 450, width=2, fill="purple")
obstacle6 = canvas.create_oval(100, 200, 150, 250, width=2, fill="blue")
obstacle7 = canvas.create_oval(530, 50, 560, 80, width=2, fill="white")

# L = (rayon) = (x1-(x0+x1)/2)
L = ( (40-(20+40)/2), (80-(70+80)/2), (510-(480+510)/2), (315-(300+315)/2), (200-(150+200)/2), (150-(100+150)/2), (560-(530+560)/2) )
# F = (xmil,ymil) 
MIL = ( ((20+40)/2, (20+40)/2), ((70+80)/2, (5+15)/2), ((480+510)/2, (510+540)/2), ((300+315)/2, (150+165)/2), ((150+200)/2, (400+450)/2), ((100+150)/2, (200+250)/2), ((530+560)/2, (50+80)/2) )

print(L)
print (MIL)

#while True :
#    robot.tourner2(3.14,0)
#    robot.nouvelle_position2(1)
#    time.sleep(5)
#    print(robot)
