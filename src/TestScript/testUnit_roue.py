import unittest
from Dexter import Roue as ro
from Dexter import constantes as c
import math

class TestRoue(unittest.TestCase):

    def setUp(self):
        """
        Permet d'enregistrer tous les attributs de Roues
        """
        self.roue1 = ro.Roue(c.RAYON_DES_ROUES_CM,c.VITESSE_MAX_TOUR_PAR_SEC)
        self.roue2 = ro.Roue(5,15)

    def test_init(self):
        self.assertEqual(self.roue1.taille_cm,1)
        self.assertEqual(self.roue2.taille_cm,5)
        self.assertEqual(self.roue1.vMaxTourParSec,30)
        self.assertEqual(self.roue2.vMaxTourParSec,15)
    def test_setVitesse(self):
        """
        """
        self.roue1.setVitesse(5)
        self.roue2.setVitesse(20)
        self.assertEqual(self.roue1.vTourParSec,(5*5)/(36*math.pi*self.roue1.taille_cm*0.01))
        self.assertEqual(self.roue2.vTourParSec,15)
    if __name__ == '__main__':
        unittest.main()
#pour tester -> python3 .m unittest nom_de_Dexter .nomdefichier -v