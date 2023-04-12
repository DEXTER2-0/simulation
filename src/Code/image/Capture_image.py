class Capture_image:
    def __init__(self,robot):
        self.robot=robot
        self.encours=True
        self.image=None
    
    def update(self):
        self.image=self.robot.get_image()
    
    def stop(self):
        self.encours=False