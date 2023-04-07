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
    obstacle4 = obs.Obstacle(1,(350,300),10)
    liste_obstacle = [obstacle4]
    #initialise le robot
    Dexter=rb.Robot(250,300)
    #initialise le terrain
    Terrain=ter.Terrain(0,cs.WIDTH,0,cs.HEIGHT, liste_obstacle)
    #commandes pour que le robot tourne
    Simu=simu.Simulation(Dexter,Terrain,120)
    #initialisation le traducteur 
    trad = tr.Traducteur_Simulation(Dexter,Simu)
    def condition():
        if trad.capteur()>10:
            return False
        return True

    test = []
    for i in range(4):
        
        strat_evite = ia.IAConditionnel(trad,ia.IA_avancer(trad, 400, 100),ia.IA_tourner(trad, 90,0))
        #test.append(strat_tourne)
        test.append(strat_evite)


    IA_tourne = ia.IA_tourner(trad,90,1)
    #commandes pour que le robot avance
    IA_avance = ia.IA_avancer(trad,10,100)
    ia_avance=ia.IA_avancer(trad,10,100)
    Affichage=af.Affichage(Simu,60)
    #IA_evite = ia.IA_eviter(trad,I_avance,IA_tourne,10)
    #IA = ia.IA(trad,[IA_tourne],0.01)
    #IA = ia.IA([ia_avance,IA_tourne,IA_avance],120)
    #IA = ia.IA(Dexter,[IA_evite],0.01)
    IA = ia.IA(test, 120)
    Affichage.start()
    Simu.start()
    IA.start()
