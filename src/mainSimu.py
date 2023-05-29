from Code.simulation import Simulation  as simu
from Code.simulation import constantes as cs
from Code.simulation import Robot as rb
from Code.simulation  import Obstacle as obs
from Code.ia import Traducteur_proxy as proxy
from Code.ia  import IA as ia
from Code.affichage import affichage as af
from Code.simulation  import Terrain as ter
from math import radians
from time import time as time
import logging

if __name__=='__main__':
    FORMAT = "[%(levelname)s] %(message)s"
    logging.basicConfig(format=FORMAT, level=logging.DEBUG)
    #cree les obstacles
    obstacle4 = obs.Obstacle(1,(300,200),10)
    liste_obstacle = [obstacle4]
    #initialise le robot
    Dexter=rb.Robot(cs.RAYON_DES_ROUES_CM,cs.RAYON_ROBOT_CM,cs.DISTANCE_CAPTABLE)
    #initialise le terrain
    Terrain=ter.Terrain(0,cs.WIDTH,0,cs.HEIGHT, liste_obstacle)
    Simu=simu.Simulation(Dexter,Terrain,60)
    #initialisation le traducteur 
    trad=proxy.Traducteur(Dexter,Simu,True)
    #initialisation de l'affichage
    Affichage=af.Affichage(Simu,60,cs.WIDTH,cs.HEIGHT)
    #commandes pour que le robot fasse un carre
    test = []
    for i in range(4):
        strat_avance = ia.IA_avancer(trad,20,300)
        strat_tourne = ia.IA_tourner(trad,90,0,100)
        test.append(strat_avance)
        test.append(strat_tourne)
    strat_evite = ia.IAConditionnel(trad,ia.IA_avancer(trad,400,100),ia.IA_tourner(trad, 90,1,100))
    IA_tourne = ia.IA_tourner(trad,90,1,100)
    #commandes pour que le robot avance le plus proche d'un obstacle 
    IA_avance = ia.IA_avancer(trad,20,300)
    test2=[strat_evite,IA_avance]
    
    #-----------------------------------------------------------------------------------
    #IA_Conditionnelle = ia.IAConditionnel(trad,IA_avance,IA_tourne)
    IA = ia.IA(test2,340)
    Affichage.start()
    Simu.start()
    IA.start()
