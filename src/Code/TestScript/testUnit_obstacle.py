import unittest
from Code.simulation.Obstacle import Obstacle 

class TestObstacle(unittest.TestCase):

    def setUp(self):
        """
        Permet d'enregistrer tous les attributs de Obstacle
        """
        self.obs1 = Obstacle(2, (5, 3),[5, 6]) #création d'un obstacle du type rectangle
        self.obs2 = Obstacle(1,(1,4),5) #création d'un obstacle du type cercle
        
    def test_init(self):
        """
        Permet de tester si les objects sont bien initialisés  
        """
        #tester pour l'objet de type obstacle
        self.assertEqual(self.obs1.type,2)
        self.assertEqual(self.obs1.longueur,5)
        self.assertEqual(self.obs1.largeur,6)
        self.assertNotEqual(self.obs1.largeur,self.obs1.longueur)       

        #self.assertEqual(self.obs2.longueur,3)
        #self.assertEqual(self.obs2.largeur,3)

    if __name__ == '__main__':
        unittest.main()
#pour tester -> python3 .m unittest nom_de_simulation .nomdefichier -v
