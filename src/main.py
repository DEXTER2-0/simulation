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
import logging

if __name__=='__main__':
    FORMAT = "[%(levelname)s] %(message)s"
    logging.basicConfig(format=FORMAT, level=logging.DEBUG)
    #cree les obstacles
    obstacle4 = obs.Obstacle(1,(590,15),10)
    obstacle1 = obs.Obstacle(1,(590,590),10)
    obstacle2 = obs.Obstacle(1,(15,15),10)
    obstacle3 = obs.Obstacle(1,(15,590),10)
    liste_obstacle = [obstacle4,obstacle1,obstacle2,obstacle3]
    #initialise le robot
    Dexter=rb.Robot(300,300)
    #initialise le terrain
    Terrain=ter.Terrain(-300,cs.WIDTH,-300,cs.HEIGHT, liste_obstacle)
    #commandes pour que le robot tourne
    Simu=simu.Simulation(Dexter,Terrain,120)
    #initialisation le traducteur 
    trad = tr.Traducteur_Simulation(Dexter)

    test = []
    #strat_1 = IA_1 = ia.IA_1(trad,ia.IA_tourner(trad,90,1),ia.IA_avancer(trad,10,100))
    #test.append(strat_1)
    for i in range(8):
        strat_avance = ia.IA_avancer(trad, 10, 100)
        strat_tourne = ia.IA_tourner(trad, 45,1)
        test.append(strat_avance)
        test.append(strat_tourne)
    #IA_tourne = ia.IA_tourner(trad,90,1)
    #commandes pour que le robot avance
    #IA_avance = ia.IA_avancer(trad,10,100)
    Affichage=af.Affichage(Simu,60,True)
    #IA_evite = ia.IA_eviter(trad,IA_avance,IA_tourne,10)
    #IA = ia.IA(trad,[IA_tourne],0.01)
    #IA = ia.IA([IA_tourne,IA_avance],120)
    #IA = ia.IA(Dexter,[IA_evite],0.01)
    IA = ia.IA(test, 120)
    Affichage.start()
    Simu.start()
    IA.start()
