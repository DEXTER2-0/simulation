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

    def getangle(self,dt,v):
        return dt*v


class Traducteur_Realite:
    def __init__(self,robot):
        self.robot=robot
    
    def setMotorDps(self,v_gauche,v_droit):
        self.robot.set_motor_dps(port,v_gauche)
    
    def getangle(self,dt):
        return dt*self.robot.get_motor_position()
