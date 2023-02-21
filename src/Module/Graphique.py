import sys
sys.path.append("../")

from Module import Simulation as simu
from Module import Robot as rb 
from TestScript import constantes as cs
from Module import Obstacle as obs
from Module import IA as ia
from Module import Terrain as ter
import time #pour pouvoir controler le temps de la boucle while True

from Module import Graphique as gr

import tkinter as tk

import time #pour pouvoir controler le temps de la boucle while True

import time #pour pouvoir controler le temps de la boucle while Truefrom math import *
from math import *


##----- Importation des Modules -----##
import tkinter as tk
 


class Graphique : 
    def __init__ (self,canvas, simulation):
        """
        Prend une simulation et une fenetre graphique de type Canvas en parametre
        """
        self.canvas = canvas
        self.simulation = simulation
        #Initialisation des coordonées a représenter graphiquement en fonction du robot de la simu
        #cercle pour le robot, et une ligne pour son orientation
        self.objet = self.canvas.create_oval(self.simulation.pos_x - self.simulation.ia.robot.rayonDuRobotCm , self.simulation.pos_y - self.simulation.ia.robot.rayonDuRobotCm,self.simulation.pos_x + self.simulation.ia.robot.rayonDuRobotCm, self.simulation.pos_y + self.simulation.ia.robot.rayonDuRobotCm, width=self.simulation.ia.robot.l, fill="red")
        self.orientation = self.canvas.create_line(self.simulation.pos_x,self.simulation.pos_y, self.simulation.pos_x+cos(self.simulation.angle)*15, self.simulation.pos_y+sin(self.simulation.angle)*15, width=2,fill="red")
        # Suppose liste d'obstacle rond Pour la représentation des obstacles de la simulation
        for i in range (len(self.simulation.terrain.liste_obstacle)):
                obs_cour = self.simulation.terrain.liste_obstacle[i]
                self.obstacle = self.canvas.create_oval(obs_cour.x-obs_cour.longueur,obs_cour.y-obs_cour.longueur,obs_cour.x+obs_cour.longueur, obs_cour.y+obs_cour.longueur, fill="red")


    def placer_robot_milieu(self,simulation):
        #Les coordonnées (Permet de placer le robot au milieu de la fenetre)
        simulation.pos_x = simulation.terrain.WIDTH_MAX/2
        simulation.pos_y = simulation.terrain.HEIGHT_MAX/2

    def update(self):
        # Récupere les coordonées du robot de la simu ainsi que son angle et les projettes graphiquement
        self.canvas.coords(self.objet,self.simulation.pos_x - self.simulation.ia.robot.rayonDuRobotCm , self.simulation.pos_y - self.simulation.ia.robot.rayonDuRobotCm,self.simulation.pos_x + self.simulation.ia.robot.rayonDuRobotCm, self.simulation.pos_y + self.simulation.ia.robot.rayonDuRobotCm)
        self.canvas.coords(self.orientation,self.simulation.pos_x,self.simulation.pos_y, self.simulation.pos_x+cos(self.simulation.angle)*15, self.simulation.pos_y+sin(self.simulation.angle)*15)

    