from Simulation import Simulation as simu
from Modele import Robot as rb
from Modele import Roue  
from Modele import constantes as cs
from Modele import Obstacle as obs
from Controleur import IA as ia
from Modele import Terrain as ter
import Graphique as gr

import tkinter as tk

import time #pour pouvoir controler le temps de la boucle while True


#Initialisation du Robot
robot = rb.Robot(cs.RAYON_DES_ROUES_CM, cs.RAYON_ROBOT_CM, 8,cs.VITESSE_MAX_TOUR_PAR_SEC)

#Initilaisation de l'IA
ia = ia.IA(robot)

#Initialisation d'une liste d'obstacle
obstacle1 = obs.Obstacle(1,30,0)
obstacle2 = obs.Obstacle(2,0,22)
obstacle3 = obs.Obstacle(3,220,1)
obstacle4 = obs.Obstacle(1,15,15)
liste_obstacle = []
liste_obstacle.append(obstacle1)
liste_obstacle.append(obstacle2)
liste_obstacle.append(obstacle3)
liste_obstacle.append(obstacle4)

#Initialisation d'un terrain
terrain = ter.Terrain(0,cs.WIDTH,0,cs.HEIGHT, liste_obstacle)

simulation = simu.Simulation(ia,robot,terrain,0.1)

fen = tk.Tk() 
canvas = tk.Canvas(fen, width = cs.WIDTH, height = cs.HEIGHT, bg = 'yellow') #fentre graphique
canvas.pack(fill="both", expand=True)

graph = gr.Graphique(canvas,simulation)
graph.placer_robot_milieu(simulation)

while True :
    simulation.update_simulation()
    graph.update()
    canvas.update()
    
   




#graph.afficher()
