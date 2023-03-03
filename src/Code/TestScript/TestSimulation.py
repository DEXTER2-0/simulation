from simulation import Simulation  as simu
from simulation import constantes as cs
from simulation  import Obstacle as obs
from ia  import IA as ia
from simulation  import Terrain as ter
from simulation import Robot as rb
#print(globals())
#from ..Code import simulation as simu
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
