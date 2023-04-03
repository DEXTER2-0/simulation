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
    obstacle1 = obs.Obstacle(1,(50,50),10)
    obstacle2 = obs.Obstacle(1,(50,550),10)
    obstacle3 = obs.Obstacle(1,(550,50),10)
    obstacle4 = obs.Obstacle(1,(550,550),10)
    liste_obstacle = [obstacle1,obstacle2,obstacle3,obstacle4]
    #initialise le robot
    Dexter=rb.Robot(300,300)
    #initialise le terrain
    Terrain=ter.Terrain(-300,cs.WIDTH,-300,cs.HEIGHT, liste_obstacle)
    #commandes pour que le robot tourne
    Simu=simu.Simulation(Dexter,Terrain,120)
    #initialisation le traducteur 
    trad = tr.Traducteur_Simulation(Dexter)
    test = []
    def hexagone():
        for i in range(6):
            if (i%2)==0:
                Dexter.dessine(True)
                print(Dexter.dessin)
                strat_tourne = ia.IA_tourner(trad, 60,1)
                strat_avance = ia.IA_avancer(trad, 10, 100)
                test.append(strat_avance)
                test.append(strat_tourne)
            elif(i%2==1):
                Dexter.dessine(False)
                print(Dexter.dessin)
                strat_tourne = ia.IA_tourner(trad, 60,1)
                strat_avance = ia.IA_avancer(trad, 10, 100)
                test.append(strat_avance)
                test.append(strat_tourne)
    #hexagone()
    test2=[]
    def un():
        strat_tourne=ia.IA_tourner(trad,90,1)
        strat_avance=ia.IA_avancer(trad,20,100)
        test2.append(strat_tourne)
        test2.append(strat_avance)
    un()
    test3=[]
    def zero():
        c=0
        while c<4:
            if (c%2==0):
                strat_tourne=ia.IA_tourner(trad,90,1)
                strat_avance=ia.IA_avancer(trad,20,100)
                test3.append(strat_tourne)
                test3.append(strat_avance)
            else:
                strat_tourne=ia.IA_tourner(trad,90,1)
                strat_avance=ia.IA_avancer(trad,5,100)
                test3.append(strat_tourne)
                test3.append(strat_avance)
            c+=1
    zero()
    def alternance():
        IA=ia.IA(test2,120) #un
        IA = ia.IA(test3, 120) #zero
    alternance()
    def ligne():
        while Dexter.pos_roue_g<cs.WIDTH:
            alternance()
    ligne()
    IA_tourne = ia.IA_tourner(trad,90,1)
    #commandes pour que le robot avance
    IA_avance = ia.IA_avancer(trad,10,100)
    Affichage=af.Affichage(Simu,60)
    #IA=ia.IA(test,120) hexagone
    IA=ia.IA(test2,120) #un
    IA = ia.IA(test3, 120) #zero
    Affichage.start()
    Simu.start()
    IA.start()
