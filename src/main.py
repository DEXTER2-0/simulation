from Code.simulation import Simulation  as simu
from Code.simulation import constantes as cs
from Code.simulation  import Obstacle as obs
from Code.ia import Traducteur_proxy as proxy
from Code.ia  import IA as ia
from Code.affichage import affichage as af
from Code.simulation  import Terrain as ter
from Code.ia.robot2IN013 import Robot2IN013 
from Code.image import Capt
from Code.image.Capture_image import Traitement_image 
from Code.image import Decision 
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
    Simu=simu.Simulation(Dexter,Terrain,120)
    #initialisation le traducteur 
    trad=proxy.Traducteur(Dexter,Simu,False)
    cam = Capt(Dexter)
    tim = Traitement_image()
    des = Decision(Dexter,trad)
    #commandes pour que le robot fasse un carre
    test = []
    for i in range(4):
        strat_avance = ia.IA_avancer(trad,30,200)
        strat_tourne = ia.IA_tourner(trad,90,1,1000)
        test.append(strat_avance)
        test.append(strat_tourne)
    #-------------------------------
    #commandes pour que le robot avance le plus rapidement d'un mur
    test2 = []
    strat_avance2 = ia.IA_avancer(trad,100,490)
    test2.append(strat_avance2)
    #test.append(IA_avance)

    #------------------------------ Pour le traitement d'image -------------------------
    Dexter._start_recording()
    cam.update()
    tim.upload(cam.image)
    tim.convertion_png(tim.image,"~/Bureau/robot2/src/Code/1.jpg")
    #-----------------------------------------------------------------------------------

    IA = ia.IA(test,120)
    #IA = ia.IA(test2,120)
    #Affichage.start()
    #Simu.start()
    IA.start()
