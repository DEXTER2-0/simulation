import unittest
from Code.simulation import Obstacle
from Code.simulation import Robot
from Code.simulation import constantes as cs
from Code.ia import IA
from Code.ia import Capteur 

class TestIA_avancer(unittest.TestCase):

    def setUp(self):
        """
        Permet d'enregistrer tous les attributs de Obstacle
        """
        self.capteur = self.Capteur()
        self.robot1 = self.Robot(cs.RAYON_DES_ROUES_CM,cs.RAYON_ROBOT_CM, self.capteur,cs.VITESSE_MAX_DEG_PAR_SEC)
        self.ia = self.IA_avancer(self.robot1)
        
    def test_init(self):
        """
        """
        self.assertEqual() #pour le capteur
        self.assertEqual() # pour le robot 
class TestIA_tourner(unittest.TestCase):

    def setUp(self):
        """
        Permet d'enregistrer tous les attributs de Obstacle
        """
        self.capteur = self.Capteur()
        self.robot2 = self.Robot(cs.RAYON_DES_ROUES_CM,cs.RAYON_ROBOT_CM, self.capteur,cs.VITESSE_MAX_DEG_PAR_SEC)
        self.ia = self.IA_tourner(self.robot2)
        
    def test_init(self):
        """
        """
        self.assertEqual() #pour le capteur
        self.assertEqual() # pour le robot 

class TestIA_eviter(unittest.TestCase):

    def setUp(self):
        """
        Permet d'enregistrer tous les attributs de Obstacle
        """
        self.capteur = self.Capteur()
        self.robot2 = self.Robot(cs.RAYON_DES_ROUES_CM,cs.RAYON_ROBOT_CM, self.capteur,cs.VITESSE_MAX_DEG_PAR_SEC)
        self.ia = self.IA_tourner(self.robot2)
        
    def test_init(self):
        """
        """
        self.assertEqual() #pour le capteur
        self.assertEqual() # pour le robot 
    if __name__ == '__main__':
        unittest.main()
#pour tester -> python3 .m unittest nom_de_simulation .nomdefichier -v