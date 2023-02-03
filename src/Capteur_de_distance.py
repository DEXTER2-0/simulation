from math import pi,sqrt
class Capteur_de_distance :
   def __init__(self, distanceCaptable,distanceObstacle) :
       self.distanceCaptable=distanceCaptable
       self.distanceObstacle=distanceObstacle

    def distance(self,robot,obstacle):
        """
        Permet de calculer la distance entre le robot de l'obstable passés en parametre
        """
        xr = robot.pos_x
        yr = robot.pos_y
        xo = obstacle.x
        yo = obstacle.y
        return sqrt((xo-xr)**2+(yo-yr)**2)
        
      