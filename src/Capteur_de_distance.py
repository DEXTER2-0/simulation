from math import pi
class Capteur_de_distance :
   def __init__(self, distanceCaptable,distanceObstacle) :
       self.distanceCaptable=distanceCaptable
       self.distanceObstacle=distanceObstacle
    def __str__(self) :
        """
        Equivalent methode toString(Java)
        Permet de redéfinir la methode print(monInstance)
        """
        res="Capteur de distance de distance captable : " + str(self.distanceCaptable) + "cm"
        if self.distanceObstacle == 0:
            res+="  est à l'arret"
        else :
            res+="  est à " + str(self.distanceObstacle) + "cm"
        return res