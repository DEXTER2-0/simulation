import unittest
from Code.simulation import Robot as rb
from Code.simulation import constantes as cs
from Code.simulation import Terrain as tr
from Code.ia import IA as ia
from Code.simulation import Obstacle as ob
from Code.simulation import Simulation as sm




class Test_IA(unittest.TestCase):
    def setUp(self,list_ia):
        self.robot = rb.Robot(cs.RAYON_DES_ROUES_CM,cs.RAYON_ROBOT_CM,cs.VITESSE_MAX_DEG_PAR_SEC)
        self.ia_avance = ia.IA_avancer(self.robot)
        self.ia_tourne = ia.IA_tourner(self.robot)
        self.ia_evite = ia.IA_eviter(self.robot,self.ia_avance,self.ia_tourne)
        self.list = [self.ia_avance,self.ia_tourne,self.ia_evite]
        self.ia = ia.IA(self.list)

    def test_init(self):
        self.assertIn(self.ia_evite,self.list)
        self.assertIn(self.ia_tourne,self.list)
        self.assertIn(self.ia_avance,self.list)

class TestIA_avancer(unittest.TestCase):

    def setUp(self):
        """
        Permet d'enregistrer tous les attributs de Obstacle
        """
        #self.capteur1 = rb.Capteur_de_distance(cs.DISTANCE_CAPTABLE)
        self.robot1 = rb.Robot(cs.RAYON_DES_ROUES_CM,cs.RAYON_ROBOT_CM,cs.VITESSE_MAX_DEG_PAR_SEC)
        self.ia = ia.IA_avancer(self.robot1)
        self.obs1 = ob.Obstacle(2,22,0)
        self.obs2 = ob.Obstacle(4,15,5)
        self.obs3 = ob.Obstacle(8,20,10)
        self.listObs = [self.obs1,self.obs2,self.obs3]
        self.terrain = tr.Terrain(0,cs.WIDTH,0,cs.HEIGHT,self.listObs)
        self.simu = sm.Simulation(self.robot1,self.terrain,1)
        
    def test_init(self):
        """
        """
        self.assertEqual(self.robot1.roue_gauche.taille_cm,cs.RAYON_DES_ROUES_CM) # pour le robot
        self.assertEqual(self.robot1.roue_gauche.taille_cm,self.robot1.roue_droite.taille_cm)
        self.assertEqual(self.robot1.rayonDuRobotCm, cs.RAYON_ROBOT_CM)
        self.assertEqual(self.ia.robot.new_orientation, 0) 
        self.assertEqual(self.robot1.new_orientation,0)
        self.assertEqual(self.ia.robot.v,self.robot1.v)
        self.assertEqual(self.ia.robot.new_orientation,self.robot1.new_orientation)
        self.assertIn(self.obs1,self.listObs)
        self.assertIn(self.obs2,self.listObs)
        self.assertIn(self.obs3,self.listObs)

    """class TestIA_tourner(unittest.TestCase):

    def setUp(self):
        
        Permet d'enregistrer tous les attributs de Obstacle
        
        #self.capteur = self.Capteur()
        self.robot2 = self.Robot(cs.RAYON_DES_ROUES_CM,cs.RAYON_ROBOT_CM, self.capteur,cs.VITESSE_MAX_DEG_PAR_SEC)
        self.ia = self.IA_tourner(self.robot2)
        
    def test_init(self):
        
        self.assertEqual() #pour le capteur
        self.assertEqual() # pour le robot 

class TestIA_eviter(unittest.TestCase):

    def setUp(self):
        
        #self.capteur = self.Capteur()
        self.robot2 = self.Robot(cs.RAYON_DES_ROUES_CM,cs.RAYON_ROBOT_CM, self.capteur,cs.VITESSE_MAX_DEG_PAR_SEC)
        self.ia = self.IA_tourner(self.robot2)
        
    def test_init(self):
        
        
        self.assertEqual() #pour le capteur
        self.assertEqual() # pour le robot 

    """
    if __name__ == '__main__':
        unittest.main()
#pour tester -> python3 .m unittest nom_de_simulation .nomdefichier -v