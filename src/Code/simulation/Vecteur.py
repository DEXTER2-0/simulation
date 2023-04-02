from math import radians, degrees, sqrt, acos, cos, sin

class Point:
    def __init__(self, x, y):
        """
        :param x: abscisse du point
        :param y: ordonnée du point
        """
        self.x = x
        self.y = y
    
    def __add__(self, p2):
        """
        :param p2: deuxieme point
        """
        if isinstance(p2, Vecteur): # Application d'un vecteur à un point
            return Point(self.x + p2.vect[0], self.y + p2.vect[1])
        return Point(self.x + p2.x, self.y + p2.y)
    
    def distance(self, p2):
        """
        :param p2: deuxième point
        Distance entre les deux points
        """
        return sqrt((self.x - p2.x)**2 + (self.y - p2.y)**2)

    def rotation(self, centre, angle):
        """
        :param centre: centre de la rotation
        :param angle: angle de la rotation
        """
        distance = self.distance(centre)
        vect_src = Vecteur(centre, self)
        angle_vect_dest = Vecteur.get_vect_from_angle(0).angle_sign(vect_src) + angle
        vect_dest = Vecteur.get_vect_from_angle(angle_vect_dest)
        self.x = centre.x + vect_dest.vect[0] * distance
        self.y = centre.y + vect_dest.vect[1] * distance

class Vecteur:
    def __init__(self, p1, p2):
        """
        :param p1: point 1
        :param p2: point 2
        """
        self.vect = (p2.x - p1.x, p2.y - p1.y)
    
    
    def __mul__(self, v2):
        """
        :param v2: deuxieme vecteur
        """
        if not isinstance(v2, Vecteur): # Mutiplicaiton par un scalaire
            return Vecteur(Point(0, 0), Point(self.vect[0] * v2, self.vect[1] * v2))
        return self.vect[0] * v2.vect[0] + self.vect[1] * v2.vect[1]

    def get_vect_from_angle(angle):
        """
        :param angle: angle
        Vecteur direction depuis un angle
        """
        angle = radians(angle)
        return Vecteur(Point(0, 0), Point(round(cos(angle), 2), round(sin(angle), 2)))
    def norme(self):
        return sqrt(self.vect[0]**2 + self.vect[1] ** 2)
    
    def pointer_vers(self):
        return Point(self.vect[0], self.vect[1])
    

    def angle(self, v2):
        """
        :v2: un autre vecteur
        renvoie l'angle entre deux vecteurs
        """
        norme = self.norme() * v2.norme()
        if(norme == 0):
            return 0
        return round(degrees(acos(round((self * v2) / norme, 5))), 2)
    
    def signe(self, v2):
        """
        :v2: autre vecteur
        renvoie signe de l'angle entre deux vecteurs
        """
        return self.vect[0] * v2.vect[1] - self.vect[1] * v2.vect[0]

    def signe_angle(self, v2):
        """
        v2: autre vecteur
        Retourne l'angle signe entre les deux vecteurs
        """
        ang = self.angle(v2)
        return ang if self.sign(v2) >= 0 else - ang

    def milieu(p1,p2):
        """
        :param p1: premier point
        :param p2: deuxieme point
        """
        return Point((p1.x+p2.x)/2,(p1.y+p2.y)/2)
