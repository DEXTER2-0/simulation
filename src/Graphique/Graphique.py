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
from tkinter import Tk
from tkinter import Canvas 

fen = Tk() 
canvas = Canvas(fen, width = cs.WIDTH, height = cs.HEIGHT, bg = 'yellow') #fentre graphique

class Graphique : 
    def __init__ (self, simulation):
        self.simulation=simulation
       
    def placer_robot_milieu(self,simulation):
        #Les coordonnées (Permet de placer le robot au milieu de la fenetre)
        simulation.ia.pos_x = simulation.terrain.WIDTH_MAX/2
        simulation.ia.pos_y = simulation.terrain.HEIGHT_MAX/2

    def lancer_fenetre(self):
        ##----- Création de la fenetre -----##
        #fen = Tk() 
        #canvas = Canvas(fen, width = cs.WIDTH, height = cs.HEIGHT, bg = 'yellow') #fentre graphique
        canvas.pack(fill="both", expand=True)
        self.representation_robot = canvas.create_oval(self.simulation.ia.pos_x - self.simulation.ia.robot.rayonDuRobotCm , self.simulation.ia.pos_y - self.simulation.ia.robot.rayonDuRobotCm,self.simulation.ia.pos_x + self.simulation.ia.robot.rayonDuRobotCm, self.simulation.ia.pos_y + self.simulation.ia.robot.rayonDuRobotCm, width=self.simulation.ia.robot.l, fill="red")
       
        #self.afficher()

        ##----- Programme principal -----##
        fen.mainloop()  # Boucle d'attente des événements

   


    def update(self):
        self.simulation.update()
        #Permet de représenter le robot sur tkinter
        self.representation_robot = canvas.create_oval(self.simulation.ia.pos_x - self.simulation.ia.robot.rayonDuRobotCm , self.simulation.ia.pos_y - self.simulation.ia.robot.rayonDuRobotCm,self.simulation.ia.pos_x + self.simulation.ia.robot.rayonDuRobotCm, self.simulation.ia.pos_y + self.simulation.ia.robot.rayonDuRobotCm, width=self.simulation.ia.robot.l, fill="red")

            

    def afficher():
        # variable globale qui vont etre modifié
        #global x0,y0,x1,y1,dx,dy,dROTAT,xmil,ymil
        
        #self.representation_robot = canvas.create_oval(self.simulation.ia.pos_x - self.simulation.ia.robot.rayonDuRobotCm , self.simulation.ia.pos_y - self.simulation.ia.robot.rayonDuRobotCm,self.simulation.ia.pos_x + self.simulation.ia.robot.rayonDuRobotCm, self.simulation.ia.pos_y + self.simulation.ia.robot.rayonDuRobotCm, width=self.simulation.ia.robot.l, fill="red")


       # print("robot -> x : ",robot.pos_x)
       # print("robot -> y : ",robot.pos_y)
        self.simulation.update_simulation()
        print(self.simulation.ia.pos_x)
        print(self.simulation.ia.pos_x)
        
        canvas.coords(self.representation_robot,0,0,0,0)
        #canvas.coords(orientation,robot.pos_x,robot.pos_y, robot.pos_x+cos(robot.angle)*15, robot.pos_y+sin(robot.angle)*15)

        #canvas.after(1,afficher)


#afficher()


    #def initialiser():
        # Permet de représenter le robot sur tkinter
     #   representation_robot = canvas.create_oval(ia.pos_x - ia.rayonDuRobotCm , ia.pos_y - ia.rayonDuRobotCm,ia.pos_x + ia.robot.rayonDuRobotCm, ia.pos_y + ia.robot.rayonDuRobotCm, width=ia.robot.l, fill="purple")

        # orientation du robot
      #  orientation = canvas.create_line(ia.pos_x,ia.pos_y, ia.pos_x+cos(ia.angle)*15, ia.pos_y+sin(ia.angle)*15, width=2,fill="black")

