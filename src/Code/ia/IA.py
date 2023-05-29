from math import *
from threading import Thread
import logging
import time
from Code.simulation import constantes as cs
from abc import abstractmethod

class IA(Thread):
    def __init__(self,list_ia,fps):
        """
        :param traducteur : traducteur utilise
        :param list_ia : liste des ia utilisees
        :param dt : temps ecoule depuis le dernier calcul
        """
        super(IA, self).__init__()
        self.list_ia=list_ia
        self.ia_actuel=0
        self.fps=fps

        logging.info("IA cree")

    def run(self):
        self.encours = True
        self.list_ia[self.ia_actuel].start()
        while self.encours:   #tant qu'on run
            self.step() #on met a jour la simulation
            time.sleep(1./self.fps)
        logging.info("IA stoper")

    def step(self):
        """
        met a jour la simulation selon le temps ecoule
        """
        if not self.list_ia[self.ia_actuel].encours:
            logging.debug(f"Actuel : {self.ia_actuel}")
            self.list_ia[self.ia_actuel].stop()
            self.ia_actuel+=1
            if self.ia_actuel>=len(self.list_ia):
                self.ia_actuel=0
                self.encours=False
                return
            self.list_ia[self.ia_actuel].start()
        else:
            self.list_ia[self.ia_actuel].step()

class Strat(object):
    """
    Classe abstraite representant une strategie
    """
    def __init__(self, traducteur):
        self.trad = traducteur
        self.encours = False

    def start(self) -> None:
        self.encours = True

    def stop(self) -> None:
        self.trad.stop()
        # ("i am stopped")
        self.encours = False

    @abstractmethod
    def step(self):
        pass

class IA_avancer(Strat) :
    def __init__ (self,traducteur,distance_voulue,vitesse) :
        """
        :param traducteur : traducteur utilise
        :param d_voulue : ditance voulue a effectuer en m
        """
        super().__init__(traducteur)
        self.distance=distance_voulue
        self.distance_effectue=0

        self.vitesse=vitesse
        self.encours=False

    def start(self):
        """
        Override
        """

        super().start()
        self.trad.stop()
        self.encours=True

        self.trad.debut(self,0)
        self.distance_effectue=0

    def step(self):

        if self.trad.capteur() < cs.DISTANCE_MIN_ARRET :
            self.stop() #Car / par 10
        if not self.encours:
            return

        self.distance_effectue+=self.trad.get_distance(self,0)

        if self.distance_effectue>=self.distance:
            self.stop()
            
            return
        self.trad.avance(self.vitesse)

    def stop(self) :
        self.trad.stop()
 
        self.encours = False		



class IA_tourner(Strat):
    def __init__(self,traducteur,angle_voulu,orientation,vitesse) :
        """
        :param traducteur : traducteur utilise
        :param a_voulue : angle voulu a effectuer en deg
        """
        if orientation not in [0, 1]:
            orientation = 1
        self.orientation=orientation
        self.trad=traducteur
        self.distance_effectue=0
        self.v_a=vitesse#self.trad.robot.gspeed
        self.encours=False

        if self.trad.is_simu == False : 
            self.distance = (self.trad.robot.rayonRouesCm * angle_voulu)/360 * 3.33
        else :
            self.distance=(self.trad.robot.rayonRouesCm *angle_voulu)/360
            
    def start(self):

        super().start()
        self.trad.debut(self,self.orientation)


    def step(self):
        if not self.encours:
            return

        self.distance_effectue+=self.trad.get_distance(self,self.orientation)
        if (self.distance_effectue>=self.distance):
            self.stop()
        vitesse=self.v_a
        if self.distance_effectue>self.distance/2:
             vitesse/=2
        if self.distance_effectue>self.distance * 3/4:
            if self.trad.is_simu == True:
                vitesse/=2
        self.trad.tourne(self.orientation,vitesse)


            
    def stop(self) :
        self.trad.stop()
        # ("i am stopped")
        self.encours = False
