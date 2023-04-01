import unittest
from Code.simulation.Obstacle import Obstacle 

class TestObstacle(unittest.TestCase):

    def setUp(self):
        """
        Permet d'enregistrer tous les attributs de Obstacle
        """
        self.obs1 = Obstacle(2, (5, 3),(5, 6)) #création d'un obstacle du type rectangle
        self.obs2 = Obstacle(1,(1,4),5) #création d'un obstacle du type cercle
        self.obs3 = Obstacle(0,(0,0),200)
    def test_init(self):
        """
        Permet de tester si les objects sont bien initialisés  
        """
        #tester pour l'objet de type obstacle
        self.assertEqual(self.obs1.type,2)
        self.assertEqual(self.obs1.longueur,5)
        self.assertEqual(self.obs1.largeur,6)
        self.assertNotEqual(self.obs1.largeur,self.obs1.longueur)   
        self.assertEqual(self.obs1.pos[0], 5)
        self.assertEqual(self.obs1.pos[1], 3)
        
        #tester pour l'objet de type cercle 
        self.assertEqual(self.obs2.type,1)
        self.assertEqual(self.obs2.rayon,5)
        self.assertEqual(self.obs2.pos[0],1)
        self.assertEqual(self.obs2.pos[1],4)

    if __name__ == '__main__':
        unittest.main()
#pour tester -> python3 -m unittest nomdefichier -v
