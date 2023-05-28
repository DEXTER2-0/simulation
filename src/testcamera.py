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
    #cree les obstacles
    obstacle4 = obs.Obstacle(1,(350,300),10)
    liste_obstacle = []
    #initialise le robot
    Dexter=Robot2IN013()
    Dexter._start_recording()
    #initialise le terrain
    Terrain=ter.Terrain(0,cs.WIDTH,0,cs.HEIGHT, liste_obstacle)
    #commandes pour que le robot tourne
    Simu=simu.Simulation(Dexter,Terrain,120)
    #initialisation le traducteur 
    #trad = tr.Traducteur_Simulation(Dexter,Simu)
    trad=proxy.Traducteur(Dexter,Simu,False)
    cam = Capt(Dexter)
    tim = Traitement_image()
    des = Decision(Dexter,trad)


    test = []
    strat_avance = ia.IA_avancer(trad,5,100)
    cam.update()
    tim.upload(cam.image)
    tim.convertion_png(tim.image,"/home/warintara/Bureau/robot2/src/Code/1.jpg")
    IA = ia.IA(test,120)
    IA.start()