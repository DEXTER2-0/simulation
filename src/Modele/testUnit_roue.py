import unittest
import Roue as ro
import constantes as c
import math

class TestRoue(unittest.TestCase):

    def setUp(self):
        """
        Permet d'enregistrer tous les attributs de Roues
        """
        self.roue1 = ro.Roue(c.RAYON_DES_ROUES_CM,c.VITESSE_MAX_TOUR_PAR_SEC)
        self.roue2 = ro.Roue(5,15)

    def test_init(self):
        self.assertEqual(self.roue1.taille_cm,3)
        self.assertEqual(self.roue2.taille_cm,5)
        self.assertEqual(self.roue1.vMaxTourParSec,5)
        self.assertEqual(self.roue2.vMaxTourParSec,15)
    def test_setVitesse(self):
        """
        """
        self.roue1.setVitesse(5)
        self.roue2.setVitesse(20)
        self.assertEqual(self.roue1.vTourParSec,(5*5)/(36*math.pi*self.taille_cm*0.01))
    if __name__ == '__main__':
        unittest.main()
#pour tester -> python3 .m unittest nom_de_module.nomdefichier -v