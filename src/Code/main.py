from Code.simulation import Simulation  as simu
from Code.simulation import constantes as cs
from Code.simulation  import Obstacle as obs
from Code.ia  import IA as ia
from Code.simulation  import Terrain as ter
from Code.simulation import Robot as rb
import time
#cree les obstacles
obstacle4 = obs.Obstacle(1,15,15)
liste_obstacle = [obstacle4]
#initialise le robot
Dexter=rb.Robot(cs.RAYON_DES_ROUES_CM,cs.RAYON_ROBOT_CM,cs.VITESSE_MAX_DEG_PAR_SEC)
#initialise le terrain
Terrain=ter.Terrain(0,cs.WIDTH,0,cs.HEIGHT, liste_obstacle)
#commandes pour que le robot avance
IA_avance = ia.IA_avancer(Dexter,5)
#commandes pour que le robot tourne
IA_tourne = ia.IA_tourner(Dexter,50)

IA = ia.IA(Dexter,[IA_avance,IA_tourne],0.001)

Simu=simu.Simulation(Dexter,Terrain,0.001)

Simu.start()
IA.start()