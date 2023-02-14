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
import tkinter as tk
 


class Graphique : 
    def __init__ (self,canvas, simulation):
        self.canvas = canvas
        self.simulation = simulation
        self.objet = self.canvas.create_oval(self.simulation.ia.pos_x - self.simulation.ia.robot.rayonDuRobotCm , self.simulation.ia.pos_y - self.simulation.ia.robot.rayonDuRobotCm,self.simulation.ia.pos_x + self.simulation.ia.robot.rayonDuRobotCm, self.simulation.ia.pos_y + self.simulation.ia.robot.rayonDuRobotCm, width=self.simulation.ia.robot.l, fill="red")
        self.orientation = self.canvas.create_line(self.simulation.ia.pos_x,self.simulation.ia.pos_y, self.simulation.ia.pos_x+cos(self.simulation.ia.angle)*15, self.simulation.ia.pos_y+sin(self.simulation.ia.angle)*15, width=2,fill="red")

    def placer_robot_milieu(self,simulation):
        #Les coordonnées (Permet de placer le robot au milieu de la fenetre)
        simulation.ia.pos_x = simulation.terrain.WIDTH_MAX/2
        simulation.ia.pos_y = simulation.terrain.HEIGHT_MAX/2

    def update(self):
        self.canvas.coords(self.objet,self.simulation.ia.pos_x - self.simulation.ia.robot.rayonDuRobotCm , self.simulation.ia.pos_y - self.simulation.ia.robot.rayonDuRobotCm,self.simulation.ia.pos_x + self.simulation.ia.robot.rayonDuRobotCm, self.simulation.ia.pos_y + self.simulation.ia.robot.rayonDuRobotCm)
        self.canvas.coords(self.orientation,self.simulation.ia.pos_x,self.simulation.ia.pos_y, self.simulation.ia.pos_x+cos(self.simulation.ia.angle)*15, self.simulation.ia.pos_y+sin(self.simulation.ia.angle)*15)

    