from Code.simulation import Simulation  as simu
from Code.simulation import constantes as cs
from Code.simulation  import Obstacle as obs
from Code.ia  import IA as ia
from Code.simulation  import Terrain as ter
from Code.simulation import Robot as rb
#print(globals())
#from ..Code import Code.simulation as simu



class TestSimulation():

	def __init__(self):

		obstacle = obs.Obstacle(2,22,0)
		liste_obstacle = []
		liste_obstacle.append(obstacle)
		terrain = ter.Terrain(0,cs.WIDTH,0,cs.HEIGHT, liste_obstacle)
		robot = rb.Robot(cs.RAYON_DES_ROUES_CM, cs.RAYON_ROBOT_CM,cs.VITESSE_MAX_DEG_PAR_SEC)
		self.simulation = Simulation(robot,terrain,1)

	

	
	def testCollision(self):
		robot2=rb.Robot(cs.RAYON_DES_ROUES_CM, cs.RAYON_ROBOT_CM,cs.VITESSE_MAX_DEG_PAR_SEC)
		self.assertEqual(self.simulation.collision(),0)



if __name__ == "__main__":
	import doctest
	doctest.testmod()


#obstacle4 = obs.Obstacle(1,15,15)
#liste_obstacle = []
#liste_obstacle.append(obstacle1)
#liste_obstacle.append(obstacle2)
#liste_obstacle.append(obstacle3)
#liste_obstacle.append(obstacle4)


#Initialisation d'un terrain
#terrain = ter.Terrain(0,cs.WIDTH,0,cs.HEIGHT, liste_obstacle)

#Initialisation du Robot
#robot = rb.Robot(cs.RAYON_DES_ROUES_CM, cs.RAYON_ROBOT_CM,cs.DISTANCE_CAPTABLE,cs.VITESSE_MAX_DEG_PAR_SEC)
 
#Initialisation de la simulation avec un thread
#thread_simulation = simu.Simulation(ia,robot,terrain,1)



#Initilaisation de l'IA
#list_ia = [ia.IA_avancer(robot)]
#ia_global = ia.IA(list_ia)



#thread_simulation.start()
#ia_global.start()






