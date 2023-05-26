import cv2

def couleurs_balise(couleur): #description des couleurs de la balise
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
    return lower, upper

def trouver_couleurs(image_path):
    balise = False
    nb_couleurs = 0
    image = cv2.imread(image_path)
    if image is None:
        print("Erreur : image non trouvé : ", image_path)
        return balise

    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) #conversion de l'image en une image avec des couleurs plus saturées
    for i in ["BLEU", "ROUGE", "VERT", "JAUNE"]:
        mask = cv2.inRange(hsv_image, couleurs_balise(i)[0], couleurs_balise(i)[1]) #verification que la couleur est bien celle que l'on veut
        mask = cv2.erode(mask, None, iterations=4)
        mask = cv2.dilate(mask, None, iterations=4)
        elem = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0] #nombre de contours du masque de couleur
        if len(elem) > 0: #si le masque de couleur a des contours alors il est dans l'image
            nb_couleurs += 1
    if nb_couleurs == 4: #si les quatre couleurs ont des contours alors on a la balise
        balise = True
    return balise

print(trouver_couleurs("/home/warintara/Bureau/robot2/src/Code/TestScript/redrose.jpg"))