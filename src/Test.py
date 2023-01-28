from Robot import * # Permet d'utiliser la classe Robot se trouvant dans le meme repertoire
from Roue import * # Permet d'utiliser la classe Roue se trouvant dans le meme repertoire
from math import *
from random import *

def ang(T_en_sec): # calcul vitesse angulaire
    return (2*pi/T_en_sec)*RAYON_DES_ROUES_CM*0.01


##----- Importation des Modules -----##
from tkinter import * 
from PIL import Image
from PIL import ImageTk


# Initialisation des constantes du robot
RAYON_DES_ROUES_CM = 1 # ---->  r
VITESSE_MAX_TOUR_PAR_SEC = 30
RAYON_ROBOT_CM = 8 
DISTANCE_ROUE_CENTRE_CM = 5 # ----->  l
R_G = 0
R_D = 0
ANG_G = ang(0.001)
ANG_D = ang(0.001)
##----- Création de la fenetre -----##
fen = Tk() 
WIDTH = 600
HEIGHT = 600
canvas = Canvas(fen, width = WIDTH, height = HEIGHT, bg = 'yellow')
canvas.pack(fill="both", expand=True)

ROTAT = (3*pi)/2 #position angulaire/orientation

# formule de la distance
def distance(xA, yA, p):
    """
    p est une paire (x,y)
    """
    return sqrt((p[0]-xA)**2 + (p[1]-yA)**2)



# Les coordonnées (Permet de placer le robot au milieu de la fenetre)
x0,y0 = (WIDTH/2)-10, (HEIGHT/2)-10
x1,y1 = (WIDTH/2)+10, (HEIGHT/2)+10
xmil,ymil = (x0+x1)/2, (y0+y1)/2 # milieu du robot

dx = ((RAYON_DES_ROUES_CM*0.01)/2) * ( (cos(ROTAT)*ANG_D) + cos(ROTAT)*ANG_G)
dy = ((RAYON_DES_ROUES_CM*0.01)/2) * ( (sin(ROTAT)*ANG_D) + sin(ROTAT)*ANG_G)
dROTAT = ((RAYON_DES_ROUES_CM*0.01)/2) * ((ANG_G/DISTANCE_ROUE_CENTRE_CM*0.01) - (ANG_D/DISTANCE_ROUE_CENTRE_CM*0.01))

# Le robot à déplacer
robot = canvas.create_oval(x0, y0, x1, y1, width=2, fill="red")

obstacle1 = canvas.create_oval(20, 20, 40, 40,width=2, fill="orange")
obstacle2 = canvas.create_oval(70, 5, 80, 15, width=2, fill="green")
obstacle3 = canvas.create_oval(480, 510, 510, 540, width=2, fill="pink")
obstacle4 = canvas.create_oval(300, 150, 315, 165, width=2, fill="brown")
obstacle5 = canvas.create_oval(150, 400, 200, 450, width=2, fill="purple")
obstacle6 = canvas.create_oval(100, 200, 150, 250, width=2, fill="blue")
obstacle7 = canvas.create_oval(530, 50, 560, 80, width=2, fill="white")

# L = (rayon) = (x1-(x0+x1)/2)
L = ( (40-(20+40)/2), (80-(70+80)/2), (510-(480+510)/2), (315-(300+315)/2), (200-(150+200)/2), (150-(100+150)/2), (560-(530+560)/2) )
# F = (xmil,ymil) 
MIL = ( ((20+40)/2, (20+40)/2), ((70+80)/2, (5+15)/2), ((480+510)/2, (510+540)/2), ((300+315)/2, (150+165)/2), ((150+200)/2, (400+450)/2), ((100+150)/2, (200+250)/2), ((530+560)/2, (50+80)/2) )

print(L)
print (MIL)

# orientation du robot
orientation = canvas.create_line(xmil, ymil, xmil+cos(ROTAT)*15, ymil+sin(ROTAT)*15, width=2,fill="black")
#rgauche = canvas.create_line(x0, y1, xmil+cos(ROTAT)*8, ymil+sin(ROTAT)*8, width=5,fill="blue")


def deplacer():
    # variable globale qui vont etre modifié
    global x0,y0,x1,y1,dx,dy,dROTAT,xmil,ymil,ROTAT#,ANG_G,ANG_D

    #ANG_G = 2*


    dx = ((RAYON_DES_ROUES_CM*0.01)/2) * ( (cos(ROTAT)*ANG_D) + cos(ROTAT)*ANG_G)
    dy = ((RAYON_DES_ROUES_CM*0.01)/2) * ( (sin(ROTAT)*ANG_D) + sin(ROTAT)*ANG_G)   

    #print("xmil  : ",xmil,"  ymil  : ",ymil)
    #print("dx  : ",dx,"  dy  : ",dy)

    #11canvas.coords(orientation,xmil,ymil, xmil+cos(ROTAT)*15, ymil+sin(ROTAT)*15)


    xmil = xmil + dx
    x0 = x0 + dx
    x1 = x1 + dx

    ymil = ymil + dy
    y0 = y0 + dy
    y1 = y1 + dy

    canvas.coords(orientation,xmil,ymil, xmil+cos(ROTAT)*15, ymil+sin(ROTAT)*15)
    canvas.coords(robot,x0,y0,x1,y1)
    # (rayon) = (x1-(x0+x1)/2)
    for i in range (len(MIL)):
        if distance(xmil,ymil,MIL[i]) <= L[i]+ (x1-(x0+x1)/2) :
            print("*************************************\n")
            print("******** Collision !!!!!!!  *********\n")
            print("*************************************\n")

            return
    print("Pas de collision")
    print("robot -> x : ",xmil)
    print("robot -> y : ",ymil)

    a = randint(0, 100)
    if  a < 21 : 
        ROTAT = ROTAT + 0.1
    if a > 85 : 
         ROTAT = ROTAT - 0.1
    
    if ROTAT < 0 :
        ROTAT = 2*pi
    if ROTAT > 2*pi :
        ROTAT = 0
    
   # print(ROTAT)
   # print(a)
    canvas.after(5,deplacer) # en milliseconde : --> 1000millisecondes = 1 sec
    return


##----- Création du canevas et affichage de l'image -----##
fen.title('Simulation graphique')
#dessin = Canvas(fen, width = im.size[0], height = im.size[1])
#logo1 = dessin.create_image(0,0, anchor = NW, image = logo)
#dessin.grid(row=1)

#label = Label(fen, text="Hello World")
#label.pack()




#dessin2 = Canvas(fen, width = 5, height = 4, bg = 'black')
#dessin2.grid(row = 1, column = 0, columnspan = 2, padx = 3, pady = 3)

##----- Importation de l'image avec PIL et conversion -----##
#im = Image.open('Rond_bleu.png')
#logo = ImageTk.PhotoImage(im, master=fen)
##----- Fonctions pour les boutons -----##
def action_deplacer():
    deplacer()
    return
def action_stop():
    return

##----- Création des boutons -----##
bouton_couleur = Button(fen, text="Déplacer", width=20, command=action_deplacer)
bouton_couleur.pack(pady=10)

bouton_stop = Button(fen, text="Stop", width=20, command=action_stop)
bouton_stop.pack(pady=10)

bouton_quitter = Button(fen, text='Quitter', command=fen.quit)
bouton_quitter.pack(side=BOTTOM, pady=10)

##----- Programme principal -----##
fen.mainloop()                    # Boucle d'attente des événements

## ------------------------------------------------------------------------ ##


# instanciation d'un robot, prenant en parametre les deux roue créer précédemment
robot = Robot(RAYON_DES_ROUES_CM, VITESSE_MAX_TOUR_PAR_SEC, RAYON_ROBOT_CM)
print("\ninstanciation d'un robot, avec une vitesse max des deux roues à : ",robot.roue_droite.vMaxTourParSec , "tour/sec :")


# affichage du robot
print(robot) # affichage --> Le robot en position (0,0) est à l'arret
print("\n")

distMaxPossibleEnMetre = 3
precisionArret = 0.01
intervalleDeTempsDeCheckingEnSec = 0.1 #temps (en seconde) nécéssaire au robot pour calculer sa nouvelle position
vitesseVouluKmH = 5
"""
print("Nous allons faire avancer le robot a vitesse constante, il s'arretera lorsqu'il aura atteint la limite de ", distMaxPossibleEnMetre,"m \n")
print("Le robot avancera en vérifiant a chaque ",intervalleDeTempsDeCheckingEnSec,"seconde sa position pour éviter d'aller plus loin")
print("Avec une précision de déplacement d'environ ",precisionArret,"m\n")
i = 0
while robot.pos_x < distMaxPossibleEnMetre :

    #Le robot avance a vitesse constante et verifie sa position toutes 
    #les 0.1 sec Pour vérifier s'il ne depasse pas la distance voulue
    
    robot.avancer(vitesseVouluKmH)
    robot.nouvelle_position(vitesseVouluKmH,intervalleDeTempsDeCheckingEnSec) 
    distMaxPossibleEnMetre - (distMaxPossibleEnMetre*precisionArret)
    
    if robot.pos_x > distMaxPossibleEnMetre - (distMaxPossibleEnMetre*precisionArret) :
        robot.arreter_urgence()
        break
    i += 1

if robot.pos_x > distMaxPossibleEnMetre :
    print("\n")
    print("Le robot a dépasser la distance, il n'a pas eu le temps de checker sa position a temps")

print("Le robot a atteint ", robot.pos_x,"metre en ",i,"vérifications" )
print("Maintenant ",robot)
print("\n")
"""
