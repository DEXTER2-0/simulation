from Code.simulation import Simulation  as simu
from Code.simulation import constantes as cs
from Code.simulation  import Obstacle as obs
from Code.ia import Traducteur as tr
from Code.ia  import IA as ia
from Code.affichage import affichage as af
from Code.simulation  import Terrain as ter
from Code.simulation import Robot as rb
from math import radians
from time import time as time

obstacle1 = obs.Obstacle(2,2,0)
obstacle2=obs.Obstacle(2,290,0)
obstacle3 = obs.Obstacle(290,2,0)
obstacle4 = obs.Obstacle(290,290,0)
liste_obstacle = []
for i in range(4):
	liste_obstacle.append(obstacle+i)
        #initialise le robot
Dexter=rb.Robot(cs.RAYON_DES_ROUES_CM,cs.RAYON_ROBOT_CM,cs.VITESSE_MAX_DEG_PAR_SEC,cs.DISTANCE_CAPTABLE)
	        #initialise le terrain
Terrain=ter.Terrain(0,cs.WIDTH,0,cs.HEIGHT, liste_obstacle)
Simu=simu.Simulation(Dexter,Terrain,0.1)
Affichage=af.Affichage(Simu,200)


