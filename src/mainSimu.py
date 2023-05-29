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
    obstacle4 = obs.Obstacle(1,(300,300),10)
    liste_obstacle = [obstacle4]
    #initialise le robot
    Dexter=rb.Robot(cs.RAYON_DES_ROUES_CM,cs.RAYON_ROBOT_CM,cs.DISTANCE_CAPTABLE)
    #initialise le terrain
    Terrain=ter.Terrain(0,cs.WIDTH,0,cs.HEIGHT, liste_obstacle)
    Simu=simu.Simulation(Dexter,Terrain,cs.FPS)
    #initialisation le traducteur 
    trad=proxy.Traducteur(Dexter,Simu,True)
    #initialisation de l'affichage
    Affichage=af.Affichage(Simu,cs.FPS,cs.WIDTH,cs.HEIGHT)
    #commandes pour que le robot fasse un carre
    test = []
    for i in range(4):
        strat_avance = ia.IA_avancer(trad,cs.DISTANCE_A_PARCOURIR,cs.V_ANGULAIRE)
        strat_tourne = ia.IA_tourner(trad,cs.ANGLE,0,cs.V_ANGULAIRE)
        test.append(strat_avance)
        test.append(strat_tourne)
    #commandes pour que le robot avance le plus proche d'un obstacle et de l'eviter
    test2 = []
    strat_evite = ia.IAConditionnel(trad,ia.IA_avancer(trad,cs.DISTANCE_A_PARCOURIR,cs.V_ANGULAIRE),ia.IA_tourner(trad, cs.ANGLE,1,cs.V_ANGULAIRE))
    
    IA_avance = ia.IA_avancer(trad,20,300)
    test2=[strat_evite,IA_avance]
    #commandes pour que le robot avance le plus rapidement d'un mur
    test3 = []
    IA_avance = ia.IA_avancer(trad,20,300)
    test3=[IA_avance]

    
    #-----------------------------------------------------------------------------------
    IA = ia.IA(test,cs.FPS)
    #IA = ia.IA(test2,cs.FPS)
    #IA = ia.IA(test3,cs.FPS)
    Affichage.start()
    Simu.start()
    IA.start()
