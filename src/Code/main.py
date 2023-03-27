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
#obstacle4 = obs.Obstacle(10,20,40)
liste_obstacle = []

#initialise le robot
Dexter=rb.Robot(cs.RAYON_DES_ROUES_CM,5,cs.VITESSE_MAX_DEG_PAR_SEC,cs.DISTANCE_CAPTABLE)

#initialise le terrain
Terrain=ter.Terrain(-300,cs.WIDTH,-300,cs.HEIGHT, liste_obstacle)

#commandes pour que le robot tourne






Simu=simu.Simulation(Dexter,Terrain,0.01)
#initialisation le traducteur 
trad = tr.Traducteur_Simulation(Simu,Dexter)

IA_tourne = ia.IA_tourner(trad,90)

#commandes pour que le robot avance
IA_avance = ia.IA_avancer(trad,50000)

Affichage=af.Affichage(Simu,Terrain,Dexter,200)

IA = ia.IA(trad,[IA_tourne],0.01)
#IA = ia.IA(trad,[IA_avance,IA_tourne,IA_avance,IA_tourne,IA_avance,IA_tourne,IA_avance],0.01)

#IA = ia.IA(Dexter,[IA_evite],0.01)

Simu.start()
Affichage.start()
IA.start()
