from Code.ia import Traducteur_proxy as proxy
from Code.ia  import IA as ia
from Code.ia.robot2IN013 import Robot2IN013 
from Code.simulation import Simulation  as simu
from Code.simulation import constantes as cs
from Code.simulation  import Terrain as ter
from math import radians
from time import time as time
import logging

if __name__=='__main__':
    FORMAT = "[%(levelname)s] %(message)s"
    logging.basicConfig(format=FORMAT, level=logging.DEBUG)
    #initialise le robot
    Dexter=Robot2IN013()
    #initialise le terrain
    Terrain=ter.Terrain(0,cs.WIDTH,0,cs.HEIGHT,[])
    #commandes pour que le robot tourne
    Simu=simu.Simulation(Dexter,Terrain,cs.FPS)
    #initialisation le traducteur 
    trad=proxy.Traducteur(Dexter,Simu,False)
    
    #commandes pour que le robot fasse un carre
    test = []
    for i in range(4):
        strat_avance = ia.IA_avancer(trad,cs.DISTANCE_A_PARCOURIR,cs.V_ANGULAIRE)
        strat_tourne = ia.IA_tourner(trad,cs.ANGLE,cs.GAUCHE,cs.V_ANGULAIRE)
        test.append(strat_avance)
        test.append(strat_tourne)
    #-------------------------------
    #commandes pour que le robot avance le plus rapidement d'un mur
    test2 = []
    strat_evite = ia.IAConditionnel(trad,ia.IA_avancer(trad,cs.DISTANCE_A_PARCOURIR,cs.V_ANGULAIRE),ia.IA_tourner(trad, cs.ANGLE,1,cs.V_ANGULAIRE))
    strat_avance2 = ia.IA_avancer(trad,cs.DISTANCE_A_PARCOURIR,cs.V_ANGULAIRE_MAX)
    test2.append(strat_avance2)


    #------------------------------ Pour le traitement d'image -------------------------
#from Code.image import Capt
#from Code.image.Capture_image import Traitement_image 
#from Code.image import Decision 
    #cam = Capt(Dexter)
    #tim = Traitement_image()
    #des = Decision(Dexter,trad)
    #Dexter._start_recording()
    #cam.update()
    #tim.upload(cam.image)
    #tim.convertion_png(tim.image,"~/Bureau/robot2/src/Code/1.jpg")
    #-----------------------------------------------------------------------------------

    IA = ia.IA(test,cs.FPS)
    #IA = ia.IA(test2,cs.FPS)
    IA.start()
