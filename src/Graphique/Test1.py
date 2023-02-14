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
obstacle1 = obs.Obstacle(4,500,300)
obstacle2 = obs.Obstacle(6,500,500)
obstacle3 = obs.Obstacle(3,150,100)
obstacle4 = obs.Obstacle(1,200,480)
liste_obstacle = []
liste_obstacle.append(obstacle1)
liste_obstacle.append(obstacle2)
liste_obstacle.append(obstacle3)
liste_obstacle.append(obstacle4)

#Initialisation d'un terrain
terrain = ter.Terrain(0,cs.WIDTH,0,cs.HEIGHT, liste_obstacle)

#initialisation de la simulation
simulation = simu.Simulation(ia,robot,terrain,0.1)

fen = tk.Tk() 

#Initialisation de la fenêtre graphique
canvas_fenetre = tk.Canvas(fen, width = cs.WIDTH, height = cs.HEIGHT, bg = 'yellow') 
canvas_fenetre.pack(fill="both", expand=True)

#Initialisation d'un graphique récuperant les données de la simulation et les recopie sur une fentre
graph = gr.Graphique(canvas_fenetre,simulation)

#placer le robot au milieu de la fenetre
graph.placer_robot_milieu(simulation)

#Lancement de la Simulation avec un update de la partie graphique qui se met a jours quand la simulation change
while True :
    #MAJ de la simu
    simulation.update_simulation()
    #MAJ des coordonnes recu par la simulation
    graph.update()
    #MAJ de l'affichage graphique
    canvas_fenetre.update()
    
   




#graph.afficher()
