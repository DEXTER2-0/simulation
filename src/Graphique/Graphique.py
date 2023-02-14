import Simulation as simu
from Modele import Robot as rb
from Modele import Roue  
from Modele import constantes as cs
from Modele import Obstacle as obs
from Controleur import IA as ia
from Modele import Terrain as ter
import time #pour pouvoir controler le temps de la boucle while Truefrom math import *
from math import *


##----- Importation des Modules -----##
from tkinter import * 


class Graphique : 
    def __init__ (self, simulation):
        self.simulation = simulation
        self.ia = ia
        # Les coordonnées (Permet de placer le robot au milieu de la fenetre)
        simulation.ia.pos_x = simulation.terrain.WIDTH/2
        simulation.ia.pos_y = simulation.terrain.HEIGHT/2

    def lancer_fenetre():
        ##----- Création de la fenetre -----##
        fen = Tk() 
        canvas = Canvas(fen, width = cs.WIDTH, height = cs.HEIGHT, bg = 'yellow') #fentre graphique
        canvas.pack(fill="both", expand=True)
    


    #def initialiser():
        # Permet de représenter le robot sur tkinter
     #   representation_robot = canvas.create_oval(ia.pos_x - ia.rayonDuRobotCm , ia.pos_y - ia.rayonDuRobotCm,ia.pos_x + ia.robot.rayonDuRobotCm, ia.pos_y + ia.robot.rayonDuRobotCm, width=ia.robot.l, fill="purple")

        # orientation du robot
      #  orientation = canvas.create_line(ia.pos_x,ia.pos_y, ia.pos_x+cos(ia.angle)*15, ia.pos_y+sin(ia.angle)*15, width=2,fill="black")

