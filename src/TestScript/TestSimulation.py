import sys
sys.path.append("../")

from Module import Simulation as simu
from Module import Robot as rb 
import constantes as cs
from Module import Obstacle as obs
from Module import IA as ia
from Module import Terrain as ter
import time #pour pouvoir controler le temps de la boucle while True


#Initialisation du Robot
robot = rb.Robot(cs.RAYON_DES_ROUES_CM, cs.RAYON_ROBOT_CM, 8,cs.VITESSE_MAX_TOUR_PAR_SEC)

#Initilaisation de l'IA
ia = ia.IA(robot)

#Initialisation d'une liste d'obstacle
obstacle1 = obs.Obstacle(4,20,0)
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



simulation = simu.Simulation(ia,robot,terrain,1)

while True :
    simulation.update_simulation()
    time.sleep(1)