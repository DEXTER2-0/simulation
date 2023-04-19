from Code.ia import IA as ia 
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
        self.balise=False
    
    def couleurs_balise(self,couleur): #description des couleurs de la balise
        if couleur=="BLEU":
            lower=(95,100,20)
            upper=(115,255,255)
        elif couleur=="ROUGE":
            lower=(0,100,50)
            upper=(10,255,255)
        elif couleur=="VERT":
            lower=(50,50,20)
            upper=(100,255,255)
        elif couleur=="JAUNE":
            lower=(10,100,50)
            upper=(50,255,255)
        return lower,upper

    def trouver_couleurs(self,image):
        self.balise=False
        nb_couleurs=0
        image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV) #conversion de l'image en une image avec des couleurs plus staurees
        for i in ["BLEU","ROUGE","VERT","JAUNE"]:
            mask=cv2.inRange(image,self.couleurs_balise(i)[0],self.couleurs_balise(i)[1]) #verification que la couleur est bien celle que l'on veut
            mask=cv2.erode(mask,None,iterations=4)
            mask=cv2.dilate(mask,None,iterations=4)
            elem=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0] #nombre de contours du masque de couleur
            if len(elem)>0: #si le masque de couleur a des contours alors il est dans l'image
                nb_couleurs+=1
        if nb_couleurs==4: #si les quatre couleurs ont des contours alors on a la balise
            self.balise=True

class Decision:
    def __init__(self,robot,traducteur):
        self.robot=robot
        self.tourne=ia.IA_tourner(traducteur,10,1,100)
        self.cap=Capture_image(self.robot)
        self.trait=Traitement_image()
        self.encours=True
    
    def update(self):
        while self.encours:
            self.cap.update()
            self.trait.trouver_couleurs(self.cap.image)
            if self.trait.balise:
                self.stop()
            elif not self.trait.balise and not self.tourne.encours:
                self.tourne.start()
            elif not self.trait.balise and self.tourne.encours:
                self.tourne.step()
    
    def stop(self):
        self.encours=False
        self.tourne.stop()
