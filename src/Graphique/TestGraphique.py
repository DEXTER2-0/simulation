from Robot import * # Permet d'utiliser la classe Robot se trouvant dans le meme repertoire
from Roue import * # Permet d'utiliser la classe Roue se trouvant dans le meme repertoire
import time #pour pouvoir controler le temps de la boucle while True
from math import *

##----- Importation des Modules -----##
from tkinter import * 

##----- Création de la fenetre -----##
fen = Tk() 
WIDTH = 800 # axe des x
HEIGHT = 800 # axe des y
canvas = Canvas(fen, width = WIDTH, height = HEIGHT, bg = 'yellow') #fentre graphique
canvas.pack(fill="both", expand=True)

# calcul vitesse angulaire
def ang(T_en_sec):
    return (2*pi/T_en_sec)*RAYON_DES_ROUES_CM*0.01

# formule de la distance
def distance(xA, yA, xB, yB):
    return sqrt((xB-xA)**2 + (yB-yA)**2)


# Initialisation des constantes du robot
RAYON_DES_ROUES_CM = 1 # ---->  r
VITESSE_MAX_TOUR_PAR_SEC = 30 #pas encore utilisé
RAYON_ROBOT_CM = 8
DISTANCE_ROUE_CENTRE_CM = 100 # ----->  l


# Le robot à déplacer
robot = Robot(RAYON_DES_ROUES_CM, RAYON_ROBOT_CM, VITESSE_MAX_TOUR_PAR_SEC)
# Permet de représenter le robot sur tkinter
representation_robot = canvas.create_oval(robot.pos_x - robot.rayonDuRobotCm , robot.pos_y - robot.rayonDuRobotCm,robot.pos_x + robot.rayonDuRobotCm, robot.pos_y + robot.rayonDuRobotCm, width=2, fill="purple")

print(robot.rayonDuRobotCm)

# Les coordonnées (Permet de placer le robot au milieu de la fenetre)
robot.pos_x = WIDTH/2
robot.pos_y = HEIGHT/2


# Creation des obstacle (Pensez a utliser la classe Obstacle)
obstacle1 = canvas.create_oval(20, 20, 40, 40,width=2, fill="orange")
obstacle2 = canvas.create_oval(70, 5, 80, 15, width=2, fill="green")
obstacle3 = canvas.create_oval(480, 510, 510, 540, width=2, fill="pink")
obstacle4 = canvas.create_oval(300, 150, 315, 165, width=2, fill="brown")
obstacle5 = canvas.create_oval(150, 400, 200, 450, width=2, fill="purple")
obstacle6 = canvas.create_oval(100, 200, 150, 250, width=2, fill="blue")
obstacle7 = canvas.create_oval(530, 50, 560, 80, width=2, fill="white")


# L = (rayon) = (x1-(x0+x1)/2) = liste des rayons de chaque objets
L = ( (40-(20+40)/2), (80-(70+80)/2), (510-(480+510)/2), (315-(300+315)/2), (200-(150+200)/2), (150-(100+150)/2), (560-(530+560)/2) )
# MIL  = (xmil,ymil)  = Liste des milieus des obstacles 
MIL = ( ((20+40)/2, (20+40)/2), ((70+80)/2, (5+15)/2), ((480+510)/2, (510+540)/2), ((300+315)/2, (150+165)/2), ((150+200)/2, (400+450)/2), ((100+150)/2, (200+250)/2), ((530+560)/2, (50+80)/2) )

print(L)
print (MIL)

# orientation du robot
orientation = canvas.create_line(robot.pos_x,robot.pos_y, robot.pos_x+cos(robot.angle)*15, robot.pos_y+sin(robot.angle)*15, width=2,fill="black")


def afficher():
    # variable globale qui vont etre modifié
    global x0,y0,x1,y1,dx,dy,dROTAT,xmil,ymil
    
    
    robot.tourner2(200.1,200)
    robot.nouvelle_position2(1)
    #time.sleep(0.25)


    print("robot -> x : ",robot.pos_x)
    print("robot -> y : ",robot.pos_y)

    
    canvas.coords(representation_robot,robot.pos_x - robot.rayonDuRobotCm , robot.pos_y - robot.rayonDuRobotCm,robot.pos_x + robot.rayonDuRobotCm, robot.pos_y + robot.rayonDuRobotCm)
    canvas.coords(orientation,robot.pos_x,robot.pos_y, robot.pos_x+cos(robot.angle)*15, robot.pos_y+sin(robot.angle)*15)

    canvas.after(1000,afficher)


afficher()



##----- Programme principal -----##
fen.mainloop()                    # Boucle d'attente des événements


