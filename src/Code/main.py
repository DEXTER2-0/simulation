from Code.simulation import Simulation  as simu
from Code.simulation import constantes as cs
from Code.simulation  import Obstacle as obs
from Code.ia import Traducteur as tr
from Code.ia  import IA as ia
from Code.affichage import affichage as af
from Code.simulation  import Terrain as ter
from Code.simulation import Robot as rb

from time import time as time
#cree les obstacles
obstacle4 = obs.Obstacle(10,50,0)
liste_obstacle = [obstacle4]

#initialise le robot
Dexter=rb.Robot(cs.RAYON_DES_ROUES_CM,10,cs.VITESSE_MAX_DEG_PAR_SEC)

#initialise le terrain
Terrain=ter.Terrain(-300,cs.WIDTH,-300,cs.HEIGHT, liste_obstacle)
#commandes pour que le robot avance
IA_avance = ia.IA_avancer(Dexter,5000000)
#commandes pour que le robot tourne






Simu=simu.Simulation(Dexter,Terrain,0.01)
IA_tourne = ia.IA_tourner(Dexter,45,Simu)
Affichage=af.Affichage(Simu,Terrain,Dexter,260)
#IA = ia.IA(Dexter,[IA_tourne],0.01)
IA = ia.IA(Dexter,[IA_avance,IA_tourne,IA_avance,IA_tourne,IA_avance,IA_tourne,IA_avance],0.01)

IA = ia.IA(Dexter,[IA_evite],0.01)

Simu.start()
Affichage.start()
IA.start()
