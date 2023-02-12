import Simulation as simu
from Modele import Robot Roue Obstacle 
from Modele import Constantes as cs
from Controleur import IA

#Initialisation du Robot
robot = Robot(cs.RAYON_DES_ROUES_CM, cs.RAYON_ROBOT_CM, 8,cs.VITESSE_MAX_TOUR_PAR_SEC)

simulation = simu.Simulation(robot)