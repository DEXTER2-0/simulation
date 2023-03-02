from ..  import simulation as simu
from Dexter  import Robot as rb 
from Dexter import constantes as cs
from Dexter  import Obstacle as obs
from Dexter  import IA as ia
from Dexter  import Terrain as ter
import time #pour pouvoir controler le temps de la boucle while True


#Initialisation du Robot
robot = rb.Robot(cs.RAYON_DES_ROUES_CM, cs.RAYON_ROBOT_CM,cs.DISTANCE_CAPTABLE,cs.VITESSE_MAX_TOUR_PAR_SEC)

#Initilaisation de l'IA
ia = ia.IAEvite(robot)

#Initialisation d'une liste d'obstacle
#obstacle1 = obs.Obstacle(4,20,0)
obstacle2 = obs.Obstacle(2,22,0)
#obstacle3 = obs.Obstacle(3,220,1)
#obstacle4 = obs.Obstacle(1,15,15)
liste_obstacle = []
#liste_obstacle.append(obstacle1)
liste_obstacle.append(obstacle2)
#liste_obstacle.append(obstacle3)
#liste_obstacle.append(obstacle4)

#Initialisation d'un terrain
terrain = ter.Terrain(0,cs.WIDTH,0,cs.HEIGHT, liste_obstacle)



simulation = simu.Simulation(ia,robot,terrain,1)

while True :
    simulation.update_simulation()
    time.sleep(0.1)