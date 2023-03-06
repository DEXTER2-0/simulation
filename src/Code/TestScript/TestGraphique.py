
import time #pour pouvoir controler le temps de la boucle while True

from Code.simulation import Simulation as simu
from Code.simulation import Robot as rb 
from Code.simulation import constantes as cs
from Code.simulation import Obstacle as obs
from Code.ia import IA as ia
from Code.simulation import Terrain as ter

from Code.affichage  import Graphique as gr

import tkinter as tk

import time #pour pouvoir controler le temps de la boucle while True


#Initialisation du Robot
robot = rb.Robot(cs.RAYON_DES_ROUES_CM, cs.RAYON_ROBOT_CM,cs.DISTANCE_CAPTABLE ,cs.VITESSE_MAX_RAD_PAR_SEC)

#Initilaisation de l'IA
ia = ia.IA_eviter(robot)

#Initialisation d'une liste d'obstacle
obstacle1 = obs.Obstacle(8,400,300)
obstacle2 = obs.Obstacle(7,500,500)
obstacle3 = obs.Obstacle(20,150,100)
obstacle4 = obs.Obstacle(10,200,480)
liste_obstacle = []
liste_obstacle.append(obstacle1)
#liste_obstacle.append(obstacle2)
#liste_obstacle.append(obstacle3)
#liste_obstacle.append(obstacle4)

#Initialisation d'un terrain
terrain = ter.Terrain(0,cs.WIDTH,0,cs.HEIGHT, liste_obstacle)

#initialisation de la Code.simulation
Code.simulation = simu.Code.simulation(ia,robot,terrain,0.1)

fen = tk.Tk() 

#Initialisation de la fenêtre graphique
canvas_fenetre = tk.Canvas(fen, width = cs.WIDTH, height = cs.HEIGHT, bg = 'yellow') 
canvas_fenetre.pack(fill="both", expand=True)

#Initialisation d'un graphique récuperant les données de la Code.simulation et les recopie sur une fentre
graph = gr.Graphique(canvas_fenetre,Code.simulation)

#placer le robot au milieu de la fenetre
#graph.placer_robot_milieu(Code.simulation)

#Lancement de la Code.simulation avec un update de la partie graphique qui se met a jours quand la Code.simulation change
while True :
    #MAJ de la simu
    Code.simulation.update_Code.simulation()
    #MAJ des coordonnes recu par la Code.simulation
    graph.update()
    #MAJ de l'affichage graphique
    canvas_fenetre.update()
    
   




#graph.afficher()
