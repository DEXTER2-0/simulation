import unittest
from Modele import Capteur_de_distance as cap
from Modele import Robot as rob
from Modele import Obstacle as ob
from Modele import constantes as c

class TestCapteur(unittest.TestCase):

    def setUp(self):
        """
        Permet d'enregistrer tous les attributs de Capteur_de_distance
        """
        self.capteur = cap.Capteur(10)
        self.robot = rob.Robot(3,7,self.capteur,10)
        self.obs1 = ob.Obstacle(5,6,1,4) #création d'un obstacle du type rectangle
        self.obs2 = ob.Obstacle(3,5,4) #création d'un obstacle du type cercle
        self.obs3 = ob.Obstacle(50,50) #création d'un obstacle du type mur 
    def test_init(self):
        """
        """
        self.assertEqual(self.capteur.distanceCapable,10)
    def test_distance(self):
        """
        """
        self.capteur.distance(self.robot.pos_x,self.robot.pos_y,self.obs1)
        self.capteur.distance(self.robot.pos_x,self.robot.pos_y,self.obs2)
        self.capteur.distance(self.robot.pos_x,self.robot.pos_y,self.obs5)

    def test_senseurDistance(self):
        """
        """
    if __name__ == '__main__':
        unittest.main()
#pour tester -> python3 .m unittest nom_de_module.nomdefichier -v
    