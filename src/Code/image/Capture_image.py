from PIL import Image
import cv2

class Capture_image:
    def __init__(self,robot):
        self.robot=robot
        self.image=None
    
    def update(self):
        self.image=self.robot.get_image()

class Traitement_image: #traitement d'image afin de savoir si la balise entiere est dedans
    def __init__(self):
        self.image=None
        self.balise=None
    
class Decision:
    def __init__(self,robot,traducteur):
        self.robot=robot
        self.tourne=IA_tourner(traducteur,10,1,100)
        self.cap=Capture_image(self.robot)
        self.trait=Traitement_image()
        self.encours=True
    
    def update(self):
        while self.encours:
            self.cap.update()
            #traitement de l'image
            if self.trait.balise:
                self.stop()
            elif not self.trait.balise and not self.tourne.encours:
                self.tourne.start()
            elif not self.trait.balise and self.tourne.encours:
                self.tourne.step()
    
    def stop(self):
        self.encours=False
        self.tourne.stop()
