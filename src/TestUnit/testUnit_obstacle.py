import unittest
from ..Modele.Obstacle import *

class TestObstacle(unittest.TestCase):

    def setUp(self):
        """
        Permet d'enregistrer tous les attributs de Obstacle
        """
        self.obs1 = Obstacle(5,6,1,4) #création d'un obstacle du type rectangle
        self.obs2 = Obstacle(3,5,4) #création d'un obstacle du type cercle
        self.obs3 = Obstacle(50,50) #création d'un obstacle du type mur 
    def test_init(self):
        self.assertEqual(self.obs1.longueur,5)
        self.assertEqual(self.obs1.largeur,6)
        self.assertEqual(self.obs2.longueur,3)
        self.assertEqual(self.obs2.largeur,3)

    if __name__ == '__main__':
        unittest.main()
#pour tester -> python3 .m unittest nom_de_module.nomdefichier -v
