from math import *
from Code.simulation import constantes as cs
from . import Traducteur
import time as time
from threading import Thread

class IA(Thread):
	def __init__(self,traducteur,list_ia,dt):
		"""
		:param traducteur : traducteur utilise
		:param list_ia : liste des ia utilisees
		:param dt : temps ecoule depuis le dernier calcul
		"""
		super(IA, self).__init__()
		self.list_ia=list_ia
		self.dt = dt
		self.ia_actuel=0
		self.trad=traducteur

	def run(self):
		self.encours = True
		self.list_ia[self.ia_actuel].start()
		while self.encours:   #tant qu'on run 
			self._lastTime = time.time()    # on sauvegarde l'instant du run 
			time.sleep(self.dt)     #on fait un sleep de dt afin de calculer l'intervalle de temps
			self._ITemps = time.time() - self._lastTime   #on calcule l'intervalle de temps 
			self.step() #on met a jour la simulation
		self.trad.stopSim()
           
	def step(self):
		"""
		met a jour la simulation selon le temps ecoule
		"""
		if self.list_ia[self.ia_actuel].arret:
			self.list_ia[self.ia_actuel].stop()
			self.ia_actuel+=1
			if self.ia_actuel>=len(self.list_ia):
				self.ia_actuel=0
				self.encours=False
				return
			self.list_ia[self.ia_actuel].start()
		else:
			self.list_ia[self.ia_actuel].step()
			
class IA_avancer :
	def __init__ (self,traducteur,d_voulue) :
		"""
		:param traducteur : traducteur utilise
		:param d_voulue : ditance voulue a effectuer en m
		"""
		self.trad=traducteur
		self.trad.calcul_v(0,0)
		self.trad.calcul_new_orientation(0,0)
		self.arret=False	
		self.trad.resetdistance()
		self.d_voulue=d_voulue
		self.t0=0

	def start(self):
		self.t0=time.time()
		self.trad.setMotorDps(cs.V_ANGULAIRE_G,cs.V_ANGULAIRE_D)
		self.fonctionne=True
		self.arret=False
		self.trad.calcul_v(cs.V_ANGULAIRE_G,cs.V_ANGULAIRE_D)
		self.trad.calcul_new_orientation(cs.V_ANGULAIRE_G,cs.V_ANGULAIRE_D)

	def step(self):
		if self.arret:
			return
		if (self.trad.distance<self.d_voulue):
			t=time.time()
			self.dt=t-self.t0
			self.t0=t
			self.trad.getdistance(self.dt)
		else:
			self.stop()
			self.trad.resetdistance()
	
	def stop(self):
		self.trad.setMotorDps(0,0)
		self.fonctionne=False
		self.arret=True
		self.trad.calcul_v(0,0)
		self.trad.calcul_new_orientation(0,0)

class IA_tourner:
	def __init__(self,traducteur,a_voulu) :
		"""
		:param traducteur : traducteur utilise
		:param a_voulue : angle voulu a effectuer en deg
		"""
		self.trad=traducteur
		self.trad.calcul_v(0,0)
		self.trad.calcul_new_orientation(0,0)
		self.arret=False
		self.trad.resetangle()
		self.a_voulu=a_voulu
		self.t0 = 0
	
	def start(self):
		self.t0=time.time()
		self.trad.setMotorDps(cs.V_ANGULAIRE_G,-cs.V_ANGULAIRE_D)
		self.fonctionne=True
		self.arret=False
		self.trad.calcul_v(cs.V_ANGULAIRE_G,0)
		self.trad.calcul_new_orientation(cs.V_ANGULAIRE_G,0)
		
	def step(self):
		if self.arret:
			return
		if (self.trad.angle<=self.a_voulu):
			t=time.time()
			self.dt=t-self.t0
			self.t0=t
			self.trad.getangle(self.dt)
		else:
			self.stop()
			self.trad.resetangle()
	
	def stop(self):
		self.trad.setMotorDps(0,0)
		self.fonctionne=False
		self.arret=True
		self.trad.calcul_v(0,0)
		self.trad.calcul_new_orientation(0,0)
		self.arret=True

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
		self.t0=time.time()

	def step(self):
		t=time.time()
		self.dt=t-self.t0
		self.t0=t
		if(self.trad.capteur(self.dt)<=self.d_evitement) and (self.tourner.arret):
			self.tourner.start()
		elif(self.trad.capteur(self.dt)<=self.d_evitement) and (self.tourner.fonctionne):
			self.tourner.step()
		elif(self.avancer.arret) and (self.tourner.arret):
			self.avancer.start()
		else:
			self.avancer.step()

	def stop(self):
		self.avancer.stop()
		self.tourner.stop()
		self.arret=True

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