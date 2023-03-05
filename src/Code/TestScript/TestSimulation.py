from Code.simulation import Simulation  as simu
from Code.simulation import constantes as cs
from Code.simulation  import Obstacle as obs
from Code.ia  import IA as ia
from Code.simulation  import Terrain as ter
from Code.simulation import Robot as rb
#print(globals())
#from ..Code import Code.simulation as simu
#Initialisation du Robot
robot = rb.Robot(cs.RAYON_DES_ROUES_CM, cs.RAYON_ROBOT_CM,cs.DISTANCE_CAPTABLE,cs.VITESSE_MAX_DEG_PAR_SEC)

#Initilaisation de l'IA
ia_av = ia.IA_avancer(robot)
ia_tn = ia.IA_tourner(robot)
ia = ia.IA_eviter(robot,)

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



#Code.simulation = simu.Code.simulation(ia,robot,terrain,1)
