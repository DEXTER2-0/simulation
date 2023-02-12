import unittest
import Robot
import constantes as c
class TestRobot(unittest.TestCase):
    
    def setUP(self):
        """
        Permet d'enregistrer tous les attributs de Robot 
        """
        self.robot1 = Robot(c.RAYON_DES_ROUES_CM,c.RAYON_ROBOT_CM,10,c.VITESSE_MAX_TOUR_PAR_SEC)
        self.robot1 = Robot(5,10,10,6)
    def test_init(self):
        self.assertEqual(self.robot1.roue_gauche.taille_cm,3)
        self.assertEqual(self.robot1.roue_droite.taille_cm,3)
        self.assertEqual(self.robot1.roue_droite.taille_cm,self.robot1.roue_gauche.taille_cm)
        

    
