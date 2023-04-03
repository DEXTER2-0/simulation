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
    #q1-1-----------------------------------
    #cree les obstacles
    obstacle4 = obs.Obstacle(1,(550,550),10)
    obstacle1 = obs.Obstacle(1,(50,550),10)
    obstacle2 = obs.Obstacle(1,(550,50),10)
    obstacle3 = obs.Obstacle(1,(50,50),10)
    liste_obstacle = [obstacle4,obstacle2,obstacle1,obstacle3]
      #initialise le robot
    Dexter=rb.Robot(False,300,300)
      #initialise le terrain
    Terrain=ter.Terrain(-300,cs.WIDTH,-300,cs.HEIGHT, liste_obstacle)

    #q1-2---------------------------------------
    #ajout dans l'affichage la couleur orange et modifier la fonction update pour la mettre en orange
   #q1-3---------------------------------------
   #ajout de la fonction dessine
   #1-4 
   # fait la strategie
    trad = tr.Traducteur_Simulation(Dexter)
    test = []
    for i in range(6):
      strat_tourne = ia.IA_tourner(trad, 60,1)
      strat_avance = ia.IA_avancer(trad, 10, 100)
      if i==3 :
         Dexter.set_dessin(True)
      else :
         Dexter.set_dessin(False)
      test.append(strat_avance)
      test.append(strat_tourne)

   #2-1-----------------------------
   #ajout de la fonction dessine
   
      
    Simu=simu.Simulation(Dexter,Terrain,120)
    Affichage=af.Affichage(Simu,60)
    IA = ia.IA(test, 120)

    Affichage.start()
    Simu.start()
    IA.start()
    
