from Code.simulation import Simulation as simu
from Code.simulation import Robot as rb 
from Code.simulation import constantes as cs

from Code.simulation import Obstacle as obs
from Code.ia import IA as ia
from Code.simulation import Terrain as ter
#print(globals())
import time #pour pouvoir controler le temps de la boucle while Truefrom math import *
from math import *
from threading import Thread


##----- Importation des simulations -----##
import tkinter as tk
 


class Graphique(Thread) : 
    def __init__ (self,canvas, simulation):
        """
        Prend une simulation et une fenetre graphique de type Canvas en parametre
        """
        super(Graphique,self).__init__()
        self.canvas = canvas
        self.simulation = simulation
        #Initialisation des coordonées a représenter graphiquement en fonction du robot de la simu
        #cercle pour le robot, et une ligne pour son orientation
        self.robot = self.simulation.robot
        self.objet = self.canvas.create_oval(self.simulation.pos_x - self.robot.rayonDuRobotCm , self.simulation.pos_y - self.robot.rayonDuRobotCm,self.simulation.pos_x + self.robot.rayonDuRobotCm, self.simulation.pos_y + self.robot.rayonDuRobotCm, width=self.robot.l, fill="red")
        self.orientation = self.canvas.create_line(self.simulation.pos_x,self.simulation.pos_y, self.simulation.pos_x+cos(self.simulation.angle)*15, self.simulation.pos_y+sin(self.simulation.angle)*15, width=2,fill="red")
        # Suppose liste d'obstacle rond Pour la représentation des obstacles de la simulation
        for i in range (len(self.simulation.terrain.liste_obstacle)):
                obs_cour = self.simulation.terrain.liste_obstacle[i]
                self.obstacle = self.canvas.create_oval(obs_cour.x-obs_cour.longueur,obs_cour.y-obs_cour.longueur,obs_cour.x+obs_cour.longueur, obs_cour.y+obs_cour.longueur, fill="red")


    def placer_robot_milieu(self,simulation):
        """Les coordonnées (Permet de placer le robot au milieu de la fenetre)"""
        simulation.pos_x = simulation.terrain.WIDTH_MAX/2
        simulation.pos_y = simulation.terrain.HEIGHT_MAX/2
    def run(self):
         """
         Boucle de la simulation
         """
         self.encours=True
         while self.encours:
             self.update()
             time.sleep(self.simulation.dt)
             print(ici)


    def stop(self):
        self.encours=False




    def update(self):
        # Récupere les coordonées du robot de la simu ainsi que son angle et les projettes graphiquement
        self.canvas.coords(self.objet,self.simulation.pos_x - self.robot.rayonDuRobotCm , self.simulation.pos_y - self.robot.rayonDuRobotCm,self.simulation.pos_x + self.robot.rayonDuRobotCm, self.simulation.pos_y + self.robot.rayonDuRobotCm)
        self.canvas.coords(self.orientation,self.simulation.pos_x,self.simulation.pos_y, self.simulation.pos_x+cos(self.simulation.angle)*15, self.simulation.pos_y+sin(self.simulation.angle)*15)
        
    
