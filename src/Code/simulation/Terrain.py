class Terrain:
        def __init__ (self, WIDTH_MIN, WIDTH_MAX, HEIGHT_MIN, HEIGHT_MAX,liste_obstacle) :
            """
            :param WIDTH_MIN : longueur minimale du terrain
            :param WIDTH_MAX : longueur maximale du terrain
            :param HEIGHT_MIN : largeur minimale du terrain
            :param HEIGHT_MAX : largeur maximale du terrain
            :param liste_obstacle : liste des obstacles placés sur le terrain
            """
            self.WIDTH_MIN = WIDTH_MIN
            self.WIDTH_MAX = WIDTH_MAX
            self.HEIGHT_MIN = HEIGHT_MIN
            self.HEIGHT_MAX = HEIGHT_MAX
            self.liste_obstacle = liste_obstacle
    
        def getListeObstacles(self):
            return self.liste_obstacle
        
        def getObstacle(self,i):
            return self.liste_obstacle[i]

