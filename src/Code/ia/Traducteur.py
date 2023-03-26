from Code.simulation import constantes as cs

class Traducteur :
    def __init__ (self,simulation,robot_reel,robot_sim):
        self.simulation=simulation
        self.robot_reel = robot_reel
        self.robot_sim = robot_sim


class Traducteur_Simulation:
    def __init__(self,simulation,robot):
        self.simulation=simulation
        self.robot=robot
    
    def setMotorDps(self,v_gauche,v_droite):
        self.robot.setMotorDps(v_gauche,v_droite)
    
    def getdistance(self,dt):
        self.distance+=dt*cs.V_ANGULAIRE_G*cs.RAYON_ROBOT_CM*0.01*360
        return self.distance

    def resetdistance(self):
        self.distance=0

    def getangle(self,dt):
        self.angle+=dt*cs.cs.V_ANGULAIRE_G
        return self.angle
    
    def resetangle(self):
        self.angle=0


class Traducteur_Realite:
    def __init__(self,robot):
        self.robot=robot
    
    def setMotorDps(self,v_gauche,v_droit):
        self.robot.set_motor_dps(port,v_gauche)
    
    def getdistance(self,dt):
        return dt*self.robot.get_motor_position()*360*#taille de la roue en m
    
    def resetdistance(self,dt):
        self.robot.offset_motor_encoder(port, offset)

    def getangle(self,dt):
        return dt*self.robot.get_motor_position()
    
    def resetangle(self):
        self.robot.offset_motor_encoder(port, offset)
