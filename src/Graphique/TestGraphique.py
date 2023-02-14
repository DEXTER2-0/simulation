import Simulation as simu
from Modele import Robot as rb
from Modele import Roue  
from Modele import constantes as cs
from Modele import Obstacle as obs
from Controleur import IA as ia
from Modele import Terrain as ter
from Graphique import Graphique as gr

import time #pour pouvoir controler le temps de la boucle while Truefrom math import *

##----- Importation des Modules -----##
#from tkinter import * 

##----- Création de la fenetre -----##
#fen = Tk() 
#WIDTH = 800 # axe des x
#HEIGHT = 800 # axe des y
#canvas = Canvas(fen, width = WIDTH, height = HEIGHT, bg = 'yellow') #fentre graphique
#canvas.pack(fill="both", expand=True)

# calcul vitesse angulaire
def ang(T_en_sec):
    return (2*pi/T_en_sec)*RAYON_DES_ROUES_CM*0.01

# formule de la distance
def distance(xA, yA, xB, yB):
    return sqrt((xB-xA)**2 + (yB-yA)**2)


# Initialisation des constantes du robot
#RAYON_DES_ROUES_CM = 1 # ---->  r
#VITESSE_MAX_TOUR_PAR_SEC = 30 #pas encore utilisé
#RAYON_ROBOT_CM = 8
#DISTANCE_ROUE_CENTRE_CM = 100 # ----->  l


#Initialisation du Robot
robot = rb.Robot(cs.RAYON_DES_ROUES_CM, cs.RAYON_ROBOT_CM, 8,cs.VITESSE_MAX_TOUR_PAR_SEC)

#Initilaisation de l'IA
ia = ia.IA(robot)

#Initialisation d'une liste d'obstacle
obstacle1 = obs.Obstacle(1,30,0)
obstacle2 = obs.Obstacle(2,500,5)
obstacle3 = obs.Obstacle(3,220,1)
obstacle4 = obs.Obstacle(1,15,15)
liste_obstacle = []
liste_obstacle.append(obstacle1)
liste_obstacle.append(obstacle2)
liste_obstacle.append(obstacle3)
liste_obstacle.append(obstacle4)

#Initialisation d'un terrain
terrain = ter.Terrain(0,cs.WIDTH,0,cs.HEIGHT, liste_obstacle)

graphique2D = gr.Graphique(ia,robot,terrain,1)

simulation = simu.Simulation(ia,robot,terrain,1)

while True :
    simulation.update_simulation()

# Permet de représenter le robot sur tkinter
#representation_robot = canvas.create_oval(robot.pos_x - robot.rayonDuRobotCm , robot.pos_y - robot.rayonDuRobotCm,robot.pos_x + robot.rayonDuRobotCm, robot.pos_y + robot.rayonDuRobotCm, width=2, fill="purple")


#print(robot.rayonDuRobotCm)

# Les coordonnées (Permet de placer le robot au milieu de la fenetre)
#robot.pos_x = WIDTH/2
#robot.pos_y = HEIGHT/2


# Creation des obstacle (Pensez a utliser la classe Obstacle)
obstacle1 = canvas.create_oval(20, 20, 40, 40,width=2, fill="orange")
obstacle2 = canvas.create_oval(70, 5, 80, 15, width=2, fill="green")


# L = (rayon) = (x1-(x0+x1)/2) = liste des rayons de chaque objets
#L = ( (40-(20+40)/2), (80-(70+80)/2),  )
#MIL  = (xmil,ymil)  = Liste des milieus des obstacles 
#MIL = ( ((20+40)/2, (20+40)/2), ((70+80)/2, (5+15)/2))

print(L)
print (MIL)

# orientation du robot
#orientation = canvas.create_line(robot.pos_x,robot.pos_y, robot.pos_x+cos(robot.angle)*15, robot.pos_y+sin(robot.angle)*15, width=2,fill="black")


def afficher(robot):
    # variable globale qui vont etre modifié
    global x0,y0,x1,y1,dx,dy,dROTAT,xmil,ymil
    
    
    #robot.tourner2(200.1,200)
    #robot.nouvelle_position2(1)
    #time.sleep(0.25)


    print("robot -> x : ",robot.pos_x)
    print("robot -> y : ",robot.pos_y)

    
    canvas.coords(representation_robot,robot.pos_x - robot.rayonDuRobotCm , robot.pos_y - robot.rayonDuRobotCm,robot.pos_x + robot.rayonDuRobotCm, robot.pos_y + robot.rayonDuRobotCm)
    canvas.coords(orientation,robot.pos_x,robot.pos_y, robot.pos_x+cos(robot.angle)*15, robot.pos_y+sin(robot.angle)*15)

    canvas.after(1000,afficher)


afficher()







