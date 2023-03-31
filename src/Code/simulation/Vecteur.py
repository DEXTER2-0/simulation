from math import radians, degrees, sqrt, acos, cos, sin

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

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

    