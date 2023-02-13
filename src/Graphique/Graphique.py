##----- Importation des Modules -----##
from tkinter import * 

class Graphique : 
    def __init__ (self, simulation, ia, robot, terrain, duree_boucle):
        self.simulation = simulation
        self.ia = ia
        self.robot = robot
        self.terrain = terrain
        self.duree_boucle = duree_boucle