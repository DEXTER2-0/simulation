from Code.simulation import Simulation  as simu
from Code.simulation import constantes as cs
from Code.simulation import Robot as rb
from Code.simulation  import Obstacle as obs
from Code.ia import Traducteur_proxy as proxy
from Code.ia  import IA as ia
from Code.affichage import affichage as af
from Code.simulation  import Terrain as ter
#from Code.ia.robot2IN013 import Robot2IN013 
#from Code.image import Capt
#from Code.image.Capture_image import Traitement_image 
#rom Code.image import Decision 
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
    Dexter=rb.Robot(cs.RAYON_DES_ROUES_CM,cs.RAYON_ROBOT_CM,cs.DISTANCE_CAPTABLE)
    #initialise le terrain
    Terrain=ter.Terrain(-(cs.WIDTH),cs.WIDTH,-(cs.HEIGHT),cs.HEIGHT, liste_obstacle)
    #commandes pour que le robot tourne
    Simu=simu.Simulation(Dexter,Terrain,60)
    #initialisation le traducteur 
    #trad = tr.Traducteur_Simulation(Dexter,Simu)
    trad=proxy.Traducteur(Dexter,Simu,True)
    test = []
    for i in range(4):
        strat_avance = ia.IA_avancer(trad,20,300)
        strat_tourne = ia.IA_tourner(trad,90,0,100)
        test.append(strat_avance)
        test.append(strat_tourne)

    IA_tourne = ia.IA_tourner(trad,90,1,100)
    #commandes pour que le robot avance
    IA_avance = ia.IA_avancer(trad,10,300)
    #test.append(IA_avance)
    test2=[IA_tourne]
    Affichage=af.Affichage(Simu,60,cs.WIDTH,cs.HEIGHT)
    #IA_evite = ia.IA_eviter(trad,I_avance,IA_tourne,10)
    #IA = ia.IA(trad,[IA_tourne],0.01)
    #IA = ia.IA([ia_avance,IA_tourne,IA_avance],120)
    #IA = ia.IA(Dexter,[IA_evite],0.01)

    #------------------------------ Pour le traitement d'image -------------------------
    #Dexter._start_recording()
    #cam.update()
    #tim.upload(cam.image)
    #tim.convertion_png(tim.image,"~/Bureau/robot2/src/Code/1.jpg")
    #-----------------------------------------------------------------------------------

    IA = ia.IA(test,60)
    Affichage.start()
    Simu.start()
    IA.start()