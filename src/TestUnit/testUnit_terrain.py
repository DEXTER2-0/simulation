import unittest
from Modele import Terrain as t
from Modele import constantes as c

class TestTerrain(unittest.TestCase):
    def setUp(self):
        """
        Permet d'enregistrer tous les attributs de Terrain
        """
        self.terrain1 = t.Terrain(0,50,0,50,[])
        

    def test_init(self):
        """
        vérifier si les variables de SetUp ont été bien enregistré
        """
        self.assertEqual(self.terrain1.WIDTH_MIN,0)
        self.assertEqual(self.terrain1.WIDTH_MAX,50)
        self.assertEqual(self.terrain1.HEIGHT_MIN,0)
        self.assertEqual(self.terrain1.HEIGHT_MAX,50)
        self.assertListEqual(self.terrain1.liste_obstacle,[])

    if __name__ == '__main__':
        unittest.main()
#pour tester -> python3 .m unittest nom_de_module.nomdefichier -v
