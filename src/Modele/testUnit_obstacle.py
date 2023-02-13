import unittest
import Obstacle as ob
import constantes as c

class TestObstacle(unittest.TestCase):

    def setUp(self):
        """
        Permet d'enregistrer tous les attributs de Obstacle
        """
        self.obs1 = ob.Obstacle(5,6,1,4) #obstacle avec le paramètre longueur*largeur
        self.obs2 = ob.Obstacle(3,5,4) #obstacle avec le paramètre rayon
    def test_init(self):
        self.assertEqual(self.obs1.longueur,5)
        self.assertEqual(self.obs1.longueur,6)
        self.assertEqual(self.obs2.rayon,3)

    if __name__ == '__main__':
        unittest.main()
#pour tester -> python3 .m unittest nom_de_module.nomdefichier -v
#constructeur avec longueur et largeur ne marche pas ?
#si deux obstacle sont dans le meme position?