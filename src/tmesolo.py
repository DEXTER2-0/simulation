from Code.simulation import Simulation  as simu
from Code.simulation import constantes as cs
from Code.simulation  import Obstacle as obs
from Code.ia import Traducteur as tr
from Code.ia  import IA as ia
from Code.affichage import affichage as af
from Code.simulation  import Terrain as ter
from Code.simulation import Robot as rb
from Code.simulation.Simulation import emeteur
from math import radians
from time import time as time
import logging


if __name__=='__main__':
    FORMAT = "[%(levelname)s] %(message)s"
    logging.basicConfig(format=FORMAT, level=logging.DEBUG)
    emet=emeteur()
    #q1-1-----------------------------------
    #cree les obstacles
    obstacle4 = obs.Obstacle(1,(550,550),10)

    
    obstacle1 = obs.Obstacle(1,(50,550),10)
    obstacle2 = obs.Obstacle(1,(550,50),10)
    obstacle3 = obs.Obstacle(1,(50,50),10)
    #liste_obstacle = [obstacle4,obstacle2,obstacle1,obstacle3]
      #initialise le robot

    Dexter=rb.Robot(True,emet,400,400)
      #initialise le terrain
    

    #q1-2---------------------------------------
    #ajout dans l'affichage la couleur orange et modifier la fonction update pour la mettre en orange
   #q1-3---------------------------------------
   #ajout de la fonction dessine
   #1-4 
   # fait la strategie
    trad = tr.Traducteur_Simulation(Dexter)
    test = []
    #for i in range(6):
      #strat_tourne = ia.IA_tourner(trad, 60,1)
      #strat_avance = ia.IA_avancer(trad, 10, 100)
      #if i==3 :
         #Dexter.set_dessin(True)
      #else :
         #Dexter.set_dessin(False)
      #test.append(strat_avance)
      #test.append(strat_tourne)
   
   #IA = ia.IA(test, 120)

   #2-1-----------------------------

    #IA = ia.IA([ia.IA_tourner(trad, 90,0),ia.IA_avancer(trad, 10, 100)], 120)
   #2-2-----------------------------
    """strat_tourne=ia.IA_tourner(trad, 90,1)
    test.append(strat_tourne)

    for i in range(4):
      strat_tourne = ia.IA_tourner(trad, 90,1)
      strat_avance = ia.IA_avancer(trad, 10, 100)
      if i==1 or i==3 :
         strat_avance = ia.IA_avancer(trad, 5, 100)

      test.append(strat_avance)
      test.append(strat_tourne)
      
    IA = ia.IA(test, 120)"""

    #2-3-----------------------------
    """test=[ia.IA_tourner(trad, 90,1),ia.IA_avancer(trad, 10, 100)]
    strat_tourne=ia.IA_tourner(trad, 90,1)
    strat_avance = ia.IA_avancer(trad, 10, 100)
    strat_tourne2=ia.IA_tourner(trad, 90,1)
    test.append(strat_tourne)
    Dexter.set_dessin(False)
    test.append(strat_avance)
    Dexter.set_dessin(True)

    test.append(strat_tourne2)

    for i in range(3):
      strat_tourne = ia.IA_tourner(trad, 90,1)
      strat_avance = ia.IA_avancer(trad, 10, 100)
      if i==1 or i==3 :
         strat_avance = ia.IA_avancer(trad, 5, 100)

      test.append(strat_avance)
      test.append(strat_tourne)"""
    
    

    #q2-4-----------------------------------
    """chaine="01010"
    test=[]
    for i in range(len(chaine)):
      if chaine[i]=="1":
         strat_tourne=ia.IA_tourner(trad, 90,0)

         strat_avance = ia.IA_avancer(trad, 10, 100)
         test.append(strat_tourne)
         test.append(strat_avance)
         strat_tourne2=ia.IA_tourner(trad, 90,0)
         strat_avance2 = ia.IA_avancer(trad, 10, 100)
         #Dexter.set_dessin(False)
         test.append(strat_tourne2)
         
         test.append(strat_avance2)
         #Dexter.set_dessin(True)

         
      
         
      else:
        strat_tourne=ia.IA_tourner(trad, 90,1)
        test.append(strat_tourne)

        for i in range(4):
         strat_tourne = ia.IA_tourner(trad, 90,1)
         strat_avance = ia.IA_avancer(trad, 10, 100)
         if i==1 or i==3 :
            strat_avance = ia.IA_avancer(trad, 5, 100)

         test.append(strat_avance)
         test.append(strat_tourne) 

        strat_avance1=ia.IA_avancer(trad, 10,100)
        strat_tourne2=ia.IA_tourner(trad, 90,1)
        strat_avance = ia.IA_avancer(trad, 10, 100)
        strat_avance3 = ia.IA_avancer(trad, 10, 100)

      
        test.append(strat_avance1)
        Dexter.set_dessin(False)
        test.append(strat_tourne2)
        test.append(strat_avance)
        Dexter.set_dessin(True)
        test.append(strat_avance3)"""

    #3-1 ajout d'une classe emmeteur et de la fonction get_signal      
    #3-2
    """obsa=obs.Obstacle(1,(emet.x,emet.y),emet.rayon)
    liste_obstacle=[obsa]
    distance=Dexter.get_signal()
    d=distance
    while distance!=0 :
      if (d>=distance):
         strat_tourne=ia.IA_tourner(trad, 90,1)
         strat_avance = ia.IA_avancer(trad, 10, 100)
         test.append(strat_avance)
         test.append(strat_tourne)
      else :
         strat_avance = ia.IA_avancer(trad, 10, 100)
         test.append(strat_avance)
      distance=Dexter.get_signal()
      d=distance"""


    IA = ia.IA(test, 120)


       


    Terrain=ter.Terrain(-300,cs.WIDTH,-300,cs.HEIGHT, liste_obstacle)



      
    Simu=simu.Simulation(Dexter,Terrain,emet,120)
    Affichage=af.Affichage(Simu,60)
   
   

    Affichage.start()
    Simu.start()
    IA.start()
    
