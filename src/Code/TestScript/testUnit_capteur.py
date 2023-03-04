import unittest
from Code.Capteur_de_distance import Capteur_de_distance as cap
from ..Dexter.Robot import Robot as rob
from ..Dexter.Obstacle import Obstacle as ob
from ..Dexter.constantes import constantes as c
from ..Controleur.IA import IA as i

class TestCapteur(unittest.TestCase):

    def setUp(self):
        """
        Permet d'enregistrer tous les attributs de Capteur_de_distance
        """
        self.capteur = cap.Capteur_de_distance(10)
        self.robot = rob.Robot(3,7,self.capteur,10)
        self.ia = i.IA(self.robot)
        self.obs1 = ob.Obstacle(5,6,1,4) #création d'un obstacle du type rectangle
        self.obs2 = ob.Obstacle(3,5,4) #création d'un obstacle du type cercle
        self.obs3 = ob.Obstacle(50,50) #création d'un obstacle du type mur
        listObs = [self.obs1,self.obs2,self.obs3]
    def test_init(self):
        self.assertEqual(self.capteur.distanceCaptable,10)

    def test_distance(self):
        self.capteur.distance(self.ia.pos_x,self.ia.pos_y,self.obs1)
        self.capteur.distance(self.ia.pos_x,self.ia.pos_y,self.obs2)
        self.capteur.distance(self.ia.pos_x,self.ia.pos_y,self.obs3)

    def test_senseurDistance(self):
        
    if __name__ == '__main__':
        unittest.main()
#pour tester -> python3 .m unittest nom_de_Dexter .nomdefichier -v
    