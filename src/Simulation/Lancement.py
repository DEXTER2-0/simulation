import Simulation as simu
from Modele import Robot Roue  
from Modele import Constantes as cs
from Modele import Obstacle as obs
from Controleur import IA as ia
from Modele import Terrain as ter

#Initialisation du Robot
robot = Robot(cs.RAYON_DES_ROUES_CM, cs.RAYON_ROBOT_CM, 8,cs.VITESSE_MAX_TOUR_PAR_SEC)

#Initialisation d'un terrain
terrain = ter.Terrain(0,600,0,600)



#Initialisation d'une liste d'obstacle
obstacle1 = obs.Obstacle(1,3000,1)
obstacle2 = obs.Obstacle(2,500,5)
obstacle3 = obs.Obstacle(3,2200,1)
obstacle4 = obs.Obstacle(1,15,15)
liste_obstacle = []
liste_obstacle.append(obstacle1)
liste_obstacle.append(obstacle2)
liste_obstacle.append(obstacle3)
liste_obstacle.append(obstacle4)


simulation = simu.Simulation(robot,terrain,liste_obstacle,1)