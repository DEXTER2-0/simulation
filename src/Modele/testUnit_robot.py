import unittest
import Robot as r
import constantes as c
class TestRobot(unittest.TestCase):
    
    def setUp(self):
        """
        Permet d'enregistrer tous les attributs de Robot 
        """
        self.r1 = r.Robot(c.RAYON_DES_ROUES_CM,c.RAYON_ROBOT_CM,10,c.VITESSE_MAX_TOUR_PAR_SEC)
        self.r2 = r.Robot(5,10,10,6)
    def test_init(self):
        self.assertEqual(self.r1.roue_gauche.taille_cm,3)
        self.assertEqual(self.r1.roue_droite.taille_cm,3)
        self.assertEqual(self.r1.roue_droite.taille_cm,self.r1.roue_gauche.taille_cm)
    
    if __name__ == '__main__':
        unittest.main()

    
