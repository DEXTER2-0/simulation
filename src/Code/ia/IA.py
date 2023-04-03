from math import *
from Code.simulation import constantes as cs
from . import Traducteur
from threading import Thread
import logging
import time
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
    Classe abstraite représentant une stratégie
    """

    def __init__(self, traducteur):
        self.trad = traducteur

        self.encours = False

    def start(self) -> None:
        self.encours = True

    def stop(self) -> None:
        self.trad.stop()
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

	def start(self):
		"""
		Override
		"""

		super().start()
		self.trad.stop()

		self.trad.debut(self,0)
		self.distance_effectue=0

	def step(self):
		if not self.encours:
			return
		
		self.distance_effectue+=self.trad.getdistance(self,0)

		if self.distance_effectue>=self.distance:
			self.stop()
			return
		self.trad.avance(self.vitesse)
	


class IA_tourner(Strat):
	def __init__(self,traducteur,angle_voulu,orientation) :
		"""
		:param traducteur : traducteur utilise
		:param a_voulue : angle voulu a effectuer en deg
		"""
		if orientation not in [0, 1]:
			orientation = 1
		self.orientation=orientation
		self.trad=traducteur
		self.distance=(cs.RAYON_DES_ROUES_CM *angle_voulu)/360
		self.distance_effectue=0
		self.v_a=cs.V_ANGULAIRE_G
	
	def start(self):
		
		super().start()
		self.trad.debut(self,self.orientation)


		
	def step(self):
		if not self.encours:
			return
		self.distance_effectue+=self.trad.getdistance(self,self.orientation)
		if (self.distance_effectue>=self.distance):
			self.stop()
			self.turned = True
		vitesse=self.v_a
		if self.distance_effectue>self.distance/2:
			vitesse/=2
		if self.distance_effectue>self.distance * 3/4:
			vitesse/=2
		self.trad.tourne(self.orientation,vitesse)
		

			
			


class IA_eviter:
	def __init__ (self,traducteur,IA_avancer,IA_tourner,d_evitement) :
		"""
		:param traducteur : traducteur utilise
		:param IA_avancer : IA qui donne les ordres pour avancer
		:param IA_tourner : IA qui donne les ordres pour tourner
		:param d_evitement : distance voulue entre l'obstacle et le robot lors de l'evitement
		"""
		self.trad=traducteur
		self.avancer=IA_avancer
		self.tourner=IA_tourner
		self.arret=False
		self.d_evitement=d_evitement

	def start(self):
		self.avancer.start()

	def step(self):
		if(self.trad.capteur()<=self.d_evitement) and (self.tourner.arret):
			self.tourner.start()
		elif(self.trad.capteur()<=self.d_evitement) and (self.tourner.fonctionne):
			self.tourner.step()
		elif(self.avancer.arret) and (self.tourner.arret):
			self.avancer.start()
		else:
			self.avancer.step()

	def stop(self):
		self.avancer.stop()
		self.tourner.stop()
		self.arret=True

class IA_1(Strat): 
	def __init__ (self,traducteur,ia_avance,ia_tourne) :
		"""
		:param traducteur : traducteur utilise
		:param d_voulue : ditance voulue a effectuer en m
		"""
		self.trad= traducteur
		self.avance = ia_avance
		self.tourne = ia_tourne

	def start(self):
		"""
		Override
		"""

		super().start()
		self.trad.stop()

		self.trad.debut(self,0)
		self.distance_effectue=0
		self.tourne.start()
		self.avance.start()

	def step(self):

		self.tourne.distance_effectue+=self.tourne.trad.getdistance(self,self.tourne.orientation)
		if (self.tourne.distance_effectue>=self.tourne.distance):
			self.stop()
			self.turned = True
		vitesse=self.tourne.v_a
		if self.tourne.distance_effectue>self.tourne.distance/2:
			vitesse/=2
		if self.tourne.distance_effectue>self.tourne.distance * 3/4:
			vitesse/=2
		self.tourne.trad.tourne(self.orientation,vitesse)
		

		if self.avance.distance_effectue>=self.avance.distance:
			self.avance.stop()
			return
		self.trad.avance(self.vitesse)
	
		

class IA_0(Strat): 
	def __init__ (self,traducteur,ia_avance,ia_tourne) :
		"""
		:param traducteur : traducteur utilise
		:param d_voulue : ditance voulue a effectuer en m
		"""
		self.trad= traducteur
		self.avance = ia_avance
		self.tourne = ia_tourne

	def start(self):
		"""
		Override
		"""

		super().start()
		self.trad.stop()

		self.trad.debut(self,0)
		self.distance_effectue=0

	def step(self):
		self.tourne.start()
		self.avance.start()

		self.tourne.step()
		done = True
		if(done==True ):
			self.avance.step()
	
class IA_conditionnelle:
	def __init__(self,traducteur,IA_base,IA_alternative,condition):
		"""
		:param traducteur : traducteur utilise
		:param IA_base : IA avant que la condition soit satisfaite
		:param IA_alternative : IA apres que la condition soit satisfaite
		:param condition : condition qui declenche le changement d'IA
		"""
		self.trad=traducteur
		self.IA_base=IA_base
		self.IA_alt=IA_alternative
		self.condition=condition
		self.arret=False

	def start(self):
		self.IA_base.start()
	
	def step(self):
		if self.condition and self.IA_alt.arret:
			self.IA_base.stop()
			self.IA_alt.start()
		elif self.condition and self.IA_alt.fonctionne:
			self.IA_alt.step()
		else:
			self.IA_base.step()
	
	def stop(self):
		self.IA_base.stop()
		self.IA_alt.stop()
		self.arret=True