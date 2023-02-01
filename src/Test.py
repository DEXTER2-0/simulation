from Robot import * # Permet d'utiliser la classe Robot se trouvant dans le meme repertoire
from Roue import * # Permet d'utiliser la classe Roue se trouvant dans le meme repertoire

# Initialisation des constantes du robot
RAYON_DES_ROUES_CM = 3
VITESSE_MAX_TOUR_PAR_SEC = 5
RAYON_ROBOT_CM = 8

# instanciation d'un robot, prenant en parametre les deux roue créer précédemment
robot = Robot(RAYON_DES_ROUES_CM, VITESSE_MAX_TOUR_PAR_SEC, RAYON_ROBOT_CM)
print("instanciation d'un robot, avec une vitesse max des deux roues à ",robot.roue_droite.vMaxTourParSec , "km/h :")


# affichage du robot
print(robot) # affichage --> Le robot en position (0,0) est à l'arret
print("\n")
print(robot.est_entrain_de_rouler()) # affichage --> False
distMaxPossibleEnMetre = 10
precisionArret = 0.01
intervalleDeTempsDeCheckingEnSec = 0.1 #temps (en seconde) nécéssaire au robot pour calculer sa nouvelle position
vitesseVouluKmH = 3

print("Nous allons faire avancer le robot a vitesse constante, il s'arretera lorsqu'il aura atteint la limite de ", distMaxPossibleEnMetre,"m \n")
print("Le robot avancera en vérifiant a chaque ",intervalleDeTempsDeCheckingEnSec,"seconde sa position pour éviter d'aller plus loin")
print("Avec une précision de déplacement d'environ ",precisionArret,"m\n")
while robot.pos_x < distMaxPossibleEnMetre :
    """ 
    Le robot avance a vitesse constante et verifie sa position toutes 
    les 0.1 sec Pour vérifier s'il ne depasse pas la distance voulue
    """
    #robot.avancer(vitesseVouluKmH)
    robot.nouvelle_position(vitesseVouluKmH,intervalleDeTempsDeCheckingEnSec) 
    distMaxPossibleEnMetre - (distMaxPossibleEnMetre*precisionArret)
    
    if robot.pos_x > distMaxPossibleEnMetre - (distMaxPossibleEnMetre*precisionArret) :
        robot.arreter_urgence()
        break
if robot.pos_x > distMaxPossibleEnMetre :
    print("\n")
    print("Le robot a dépasser la distance, il n'a pas eu le temps de checker sa position a temps")

print("Le robot a atteint ", robot.pos_x,"metre")
print("Maintenant ",robot)
print("\n")

