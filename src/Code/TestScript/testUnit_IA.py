import unittest
from Code.simulation.Robot import Robot
from Code.simulation.Robot import Capteur_de_distance
from Code.simulation import constantes as cs
from Code.ia.IA import IA_avancer 
class TestIA_avancer(unittest.TestCase):

    def setUp(self):
        """
        Permet d'enregistrer tous les attributs de Obstacle
        """
        self.capteur1 = Capteur_de_distance(cs.DISTANCE_CAPTABLE)
        self.robot1 = Robot(cs.RAYON_DES_ROUES_CM,cs.RAYON_ROBOT_CM,self.capteur1,cs.VITESSE_MAX_DEG_PAR_SEC)
        self.ia = IA_avancer(self.robot1)
        self.simu 
        
    def test_init(self):
        """
        """
        self.assertEqual(self.robot1.roue_gauche.taille_cm,cs.RAYON_DES_ROUES_CM) # pour le robot
        self.assertEqual(self.robot1.roue_gauche.taille_cm,self.robot1.roue_droite.taille_cm)
        self.assertEqual(self.robot1.rayonDuRobotCm, cs.RAYON_ROBOT_CM) 
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