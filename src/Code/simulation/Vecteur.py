from math import radians, degrees, sqrt, acos, cos, sin

class Point:
    def __init__(self, x, y):
        """
        :param x: abscisse du point
        :param y: ordonnée du point
        """
        self.x = x
        self.y = y
    
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
    
    def get_vect_from_angle(self,angle):
        """
        :param angle: angle
        Vecteur direction depuis un angle
        """
        angle = radians(angle)
        return Vecteur(Point(0, 0), Point(round(cos(angle), 2), round(sin(angle), 2)))

     def pointer_vers(self):
        return Point(self.vect[0], self.vect[1])