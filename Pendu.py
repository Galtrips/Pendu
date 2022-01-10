import turtle as tl #Importer les commande turtle
compteur=0          #Insérer le compteur
drapeau=0           #Futur boucle



def debut(couleur):  #Définir le dessin du pendu par plusieurs fonction
    tl.up ()
    tl.goto(-100,-100)
    tl.down ()
    tl.forward(200)
    tl.goto(0,-100)
    tl.left(90)


def b(couleur):
    tl.forward(300)
    tl.right(90)


def dessus(couleur):
    tl.forward(300)
    tl.left(180)
    tl.forward(40)
    tl.left(90)
    tl.forward(60)
    tl.right(90)


def d(couleur):
    tl.up()
    tl.forward(15)
    tl.left(90)
    tl.forward(15)
    tl.down()
    tl.circle(15)
    tl.up()
    tl.forward(15)
    tl.left(90)
    tl.forward(15)
    tl.down()


def e(couleur):
    tl.right(90)
    tl.forward(100)
    tl.right(30)


def f(couleur):
    tl.forward(60)
    tl.backward(60)
    tl.left(60)


def g(couleur):
    tl.forward(60)
    tl.backward(60)
    tl.right(30)


def h(couleur):
    tl.backward(90)
    tl.right(30)
    tl.forward(60)
    tl.backward(60)
    tl.left(60)


def i(couleur):
    tl.forward(60)

maliste=[  ]  #Créer 3 liste pour afficher l'alphabet version numérique
malist=[  ]
malis=[  ]

maliste.append("A=1, B=2, C=3, D=4, E=5, F=6, G=7, H=8, I=9, J=10")
malist.append("K=11, L=12, M=13, N=14, O=15, P=16, Q=17, R=18, S=19, T=20")
malis.append("U=21, V=22, W=23, X=24, Y=25, Z=26")


import time     #Insérer de futur temps de pause dans le programe


print("Vous allez jouer au pendu !")
print("_____")
time.sleep(3)
print("Les lettres seront représentées comme A = 1 ... Z = 26")
print("_____")
time.sleep(4)
print("Le mot est différents en fonction du nombre aléatoire")
print("_____")
time.sleep(3)
print("Il y a alors 5 insertions de numéros : insérer les bon numéros correspondant")
print("_____")
time.sleep(5)
print("Mettre la fenettre python en minuscule à la gauche et petit en largeur !")
print("_____")
time.sleep(5)
print("Agrandir la partie Console python pour les instructions !")
print("_____")
time.sleep(5)
print("Bon jeu")
print("_____")
time.sleep(3)



from random import randint
r=randint(1,3)

if r==1:
    print("Le mot est Volcan")
    while drapeau==0:       #Boucle jusqu'à le drapeau =1

        print("___________________________________________")
        print("Veuillez patientez 2 secondes . . .")
        print("___________________________________________")

        time.sleep(2)



        print("___________________________________________")
        print(maliste)      #Afficher les 3 listes
        print(malist)
        print(malis)
        print("___________________________________________")


        time.sleep(3)
        print("Veuillez patientez . . .")
        print("___________________________________________")
        time.sleep(2)       #laisser 5 secondes d'attende dans l'execution du programe

        print("___________________________________________")
        print("Saisie de la première lettre ...")
        v=int(input())      #Les lettres V O L C A N forme le mot : elles permettent l'insertions de 5 lettres différente pour le mot
        time.sleep(1)

        print("___________________________________________")
        print("Saisie de la deuxième lettre ...")
        o=int(input())
        time.sleep(1)

        print("___________________________________________")
        print("Saisie de la troisième lettre ...")
        l=int(input())
        time.sleep(1)

        print("___________________________________________")
        print("Saisie de la quatrième lettre ...")
        c=int(input())
        time.sleep(1)

        print("___________________________________________")
        print("Saisie de la cinquième lettre ...")
        a=int(input())
        time.sleep(1)

        print("___________________________________________")
        print("Saisie de la sexième lettre ...")
        print("___________________________________________")
        n=int(input())
        time.sleep(2)




        if v==22 and o==15 and l==12 and c==3 and a==1 and n==14:       #Condition = Si toute les insertions correspondent au lettre => gagner

            compteur=10                                                 #Compteur = 10 pour pas activé les futurs partis du pendue
                                                                        #Sortir de la boucle plus tard dans le programe





        else:                                                               #Si la condition n'est pas respecter => rajouté 1 au compteur
            compteur=compteur+1



        time.sleep(2)
        print("___________________________________________")
        print("Traitement des données, Veuillez patientez . . .")
        print("___________________________________________")
        time.sleep(2)
        print("___________________________________________")
        print("vous avez selectioné :")         #Montrer les lettres selectionner !
        print("___________________________________________")

        time.sleep(2)
        print("___________________________________________")
        if v==1:                                    #définir des conditions pour affiché les bonnes lettres en fonction du nombre choisie
                                                    #Celui-ci est répéter pour les lettres d'insertion V O L C A N
            print("         A")                     #Un commentaire sera écrit à la fin de la partis d'affichage des lettres pour le reperage et passer
                                                    #cette partie sans rien rater
        if v==2:
            print("         B")

        if v==3:
            print("         C")

        if v==4:
            print("         D")

        if v==5:
            print("         E")

        if v==6:
            print("         F")

        if v==7:
            print("         G")

        if v==8:
            print("         H")

        if v==9:
            print("         I")

        if v==10:
            print("         J")

        if v==11:
            print("         K")

        if v==12:
            print("         L")

        if v==13:
            print("         M")

        if v==14:
            print("         N")

        if v==15:
            print("         O")

        if v==16:
            print("         P")

        if v==17:
            print("         Q")

        if v==18:
            print("         R")

        if v==19:
            print("         S")

        if v==20:
            print("         T")

        if v==21:
            print("         U")

        if v==22:
            print("         V")

        if v==23:
            print("         W")

        if v==24:
            print("         X")

        if v==25:
            print("         Y")

        if v==26:
            print("         Z")

        time.sleep(2)

        if o==1:
            print("         A")
        if o==2:
            print("         B")
        if o==3:
            print("         C")
        if o==4:
            print("         D")
        if o==5:
            print("         E")
        if o==6:
            print("         F")
        if o==7:
            print("         G")
        if o==8:
            print("         H")
        if o==9:
            print("         I")
        if o==10:
            print("         J")
        if o==11:
            print("         K")
        if o==12:
            print("         L")
        if o==13:
            print("         M")
        if o==14:
            print("         N")
        if o==15:
            print("         O")
        if o==16:
            print("         P")
        if o==17:
            print("         Q")
        if o==18:
            print("         R")
        if o==19:
            print("         S")
        if o==20:
            print("         T")
        if o==21:
            print("         U")
        if o==22:
            print("         V")
        if o==23:
            print("         W")
        if o==24:
            print("         X")
        if o==25:
            print("         Y")
        if o==26:
            print("         Z")

        time.sleep(2)

        if l==1:
            print("         A")
        if l==2:
            print("         B")
        if l==3:
            print("         C")
        if l==4:
            print("         D")
        if l==5:
            print("         E")
        if l==6:
            print("         F")
        if l==7:
            print("         G")
        if l==8:
            print("         H")
        if l==9:
            print("         I")
        if l==10:
            print("         J")
        if l==11:
            print("         K")
        if l==12:
            print("         L")
        if l==13:
            print("         M")
        if l==14:
            print("         N")
        if l==15:
            print("         O")
        if l==16:
            print("         P")
        if l==17:
            print("         Q")
        if l==18:
            print("         R")
        if l==19:
            print("         S")
        if l==20:
            print("         T")
        if l==21:
            print("         U")
        if l==22:
            print("         V")
        if l==23:
            print("         W")
        if l==24:
            print("         X")
        if l==25:
            print("         Y")
        if l==26:
            print("         Z")

        time.sleep(2)

        if c==1:
            print("         A")
        if c==2:
            print("         B")
        if c==3:
            print("         C")
        if c==4:
            print("         D")
        if c==5:
            print("         E")
        if c==6:
            print("         F")
        if c==7:
            print("         G")
        if c==8:
            print("         H")
        if c==9:
            print("         I")
        if c==10:
            print("         J")
        if c==11:
            print("         K")
        if c==12:
            print("         L")
        if c==13:
            print("         M")
        if c==14:
            print("         N")
        if c==15:
            print("         O")
        if c==16:
            print("         P")
        if c==17:
            print("         Q")
        if c==18:
            print("         R")
        if c==19:
            print("         S")
        if c==20:
            print("         T")
        if c==21:
            print("         U")
        if c==22:
            print("         V")
        if c==23:
            print("         W")
        if c==24:
            print("         X")
        if c==25:
            print("         Y")
        if c==26:
            print("         Z")

        time.sleep(2)


        if a==1:
            print("         A")
        if a==2:
            print("         B")
        if a==3:
            print("         C")
        if a==4:
            print("         D")
        if a==5:
            print("         E")
        if a==6:
            print("         F")
        if a==7:
            print("         G")
        if a==8:
            print("         H")
        if a==9:
            print("         I")
        if a==10:
            print("         J")
        if a==11:
            print("         K")
        if a==12:
            print("         L")
        if a==13:
            print("         M")
        if a==14:
            print("         N")
        if a==15:
            print("         O")
        if a==16:
            print("         P")
        if a==17:
            print("         Q")
        if a==18:
            print("         R")
        if a==19:
            print("         S")
        if a==20:
            print("         T")
        if a==21:
            print("         U")
        if a==22:
            print("         V")
        if a==23:
            print("         W")
        if a==24:
            print("         X")
        if a==25:
            print("         Y")
        if a==26:
            print("         Z")

        time.sleep(2)

        if n==1:
            print("         A")
        if n==2:
            print("         B")
        if n==3:
            print("         C")
        if n==4:
            print("         D")
        if n==5:
            print("         E")
        if n==6:
            print("         F")
        if n==7:
            print("         G")
        if n==8:
            print("         H")
        if n==9:
            print("         I")
        if n==10:
            print("         J")
        if n==11:
            print("         K")
        if n==12:
            print("         L")
        if n==13:
            print("         M")
        if n==14:
            print("         N")
        if n==15:
            print("         O")
        if n==16:
            print("         P")
        if n==17:
            print("         Q")
        if n==18:
            print("         R")
        if n==19:
            print("         S")
        if n==20:
            print("         T")
        if n==21:
            print("         U")
        if n==22:
            print("         V")
        if n==23:
            print("         W")
        if n==24:
            print("         X")
        if n==25:
            print("         Y")
        if n==26:
            print("         Z")                     #Fin de la partie d'affichage des lettres

        print("___________________________________________")

        time.sleep(2)
        print("___________________________________________")
        print("Vérification en cours . . .")
        print("___________________________________________")
        time.sleep(2)

        if v==22:
            print("___________________________________________")
            print("La première lettre est bonne")

        else:
            print("___________________________________________")
            print("La première lettre n'est pas bonne")                         #Dire au joueurs quelles lettres sont bonne ou mauvaise en fonction du mot choisis

        time.sleep(1)
        if o==15:
            print("___________________________________________")
            print("La deuxième lettre est bonne")
        else:
            print("___________________________________________")
            print("La deuxième lettre n'est pas bonne")

        time.sleep(1)
        if l==12:
            print("___________________________________________")
            print("La troisième lettre est bonne")
        else:
            print("___________________________________________")
            print("La troisième lettre n'est pas bonne")

        time.sleep(1)
        if c==3:
            print("___________________________________________")
            print("La quatrième lettre est bonne")
        else:
            print("___________________________________________")
            print("La quatrième lettre n'est pas bonne")

        time.sleep(1)
        if a==1:
            print("___________________________________________")
            print("La cinquième lettre est bonne")
        else:
            print("___________________________________________")
            print("La cinquième lettre n'est pas bonne")

        time.sleep(1)
        if n==14:
            print("___________________________________________")
            print("Le sixième lettre est bonne")
            print("___________________________________________")
        else:
            print("___________________________________________")
            print("La sixième lettre n'est pas bonne")                      #Fin de l'affichage  de l'ordre des lettres
            print("___________________________________________")
        print("     ")
        print("___________________________________________")
        print("Une attente de 2 secondes: Veuillez patientez . . .")
        print("___________________________________________")
        time.sleep(2)
        print("     ")








        if compteur==1:                         #En fonction du nombe de tour perdu, afficher la parti du pendu pour compléter
                                                #Il n'y a que 9 essais
            debut("red")


        if compteur==2:
            b("red")


        if compteur==3:
            dessus("red")

        if compteur==4:
            d("red")

        if compteur==5:
            e("red")

        if compteur==6:
            f("red")

        if compteur==7:
            g("red")

        if compteur==8:
            h("red")

        if compteur==9:
            i("red")
            print("___________________________________________")
            print("      PERDU")            #dire au joueur sa defaite
            print("___________________________________________")
            drapeau=1                       #Sortir alors de la boucle

        if v==22 and o==15 and l==12 and c==3 and a==1 and n==14:       #Condition = Si toute les insertions correspondent au lettre => gagner
            print("___________________________________________")
            print("Gagné")
            print("___________________________________________")
            compteur=10                                                 #Compteur = 10 pour pas activé les futurs partis du pendue
            drapeau=1


if r==2:
    print("Le mot est Couper")
    while drapeau==0:       #Boucle jusqu'à le drapeau =1

        print("___________________________________________")
        print("Veuillez patientez 5 secondes . . .")
        print("___________________________________________")

        time.sleep(5)



        print("___________________________________________")
        print(maliste)      #Afficher les 3 listes
        print(malist)
        print(malis)
        print("___________________________________________")


        time.sleep(3)
        print("Veuillez patientez . . .")
        print("___________________________________________")
        time.sleep(5)       #laisser 5 secondes d'attende dans l'execution du programe

        print("___________________________________________")
        print("Saisie de la première lettre ...")
        v=int(input())      #Les lettres V O L C A N FORMENT cette fois ci un autre mot qui n'est pas Volcan mais COUPER
        time.sleep(1)

        print("___________________________________________")
        print("Saisie de la deuxième lettre ...")
        o=int(input())
        time.sleep(1)

        print("___________________________________________")
        print("Saisie de la troisième lettre ...")
        l=int(input())
        time.sleep(1)

        print("___________________________________________")
        print("Saisie de la quatrième lettre ...")
        c=int(input())
        time.sleep(1)

        print("___________________________________________")
        print("Saisie de la cinquième lettre ...")
        a=int(input())
        time.sleep(1)

        print("___________________________________________")
        print("Saisie de la sexième lettre ...")
        print("___________________________________________")
        n=int(input())
        time.sleep(3)




        if v==3 and o==15 and l==21 and c==16 and a==5 and n==18:       #Condition = Si toute les insertions correspondent au lettre => gagner

            compteur=10                                                 #Compteur = 10 pour pas activé les futurs partis du pendue
                                                                        #Sortir de la boucle plus tard dans le programe





        else:                                                               #Si la condition n'est pas respecter => rajouté 1 au compteur
            compteur=compteur+1



        time.sleep(2)
        print("___________________________________________")
        print("Traitement des données, Veuillez patientez . . .")
        print("___________________________________________")
        time.sleep(2)
        print("___________________________________________")
        print("vous avez selectioné :")         #Montrer les lettres selectionner !
        print("___________________________________________")

        time.sleep(2)
        print("___________________________________________")
        if v==1:                                    #définir des conditions pour affiché les bonnes lettres en fonction du nombre choisie
                                                    #Celui-ci est répéter pour les lettres d'insertion V O L C A N
            print("         A")                     #Un commentaire sera écrit à la fin de la partis d'affichage des lettres pour le reperage et passer
                                                    #cette partie sans rien rater
        if v==2:
            print("         B")

        if v==3:
            print("         C")

        if v==4:
            print("         D")

        if v==5:
            print("         E")

        if v==6:
            print("         F")

        if v==7:
            print("         G")

        if v==8:
            print("         H")

        if v==9:
            print("         I")

        if v==10:
            print("         J")

        if v==11:
            print("         K")

        if v==12:
            print("         L")

        if v==13:
            print("         M")

        if v==14:
            print("         N")

        if v==15:
            print("         O")

        if v==16:
            print("         P")

        if v==17:
            print("         Q")

        if v==18:
            print("         R")

        if v==19:
            print("         S")

        if v==20:
            print("         T")

        if v==21:
            print("         U")

        if v==22:
            print("         V")

        if v==23:
            print("         W")

        if v==24:
            print("         X")

        if v==25:
            print("         Y")

        if v==26:
            print("         Z")

        time.sleep(2)

        if o==1:
            print("         A")
        if o==2:
            print("         B")
        if o==3:
            print("         C")
        if o==4:
            print("         D")
        if o==5:
            print("         E")
        if o==6:
            print("         F")
        if o==7:
            print("         G")
        if o==8:
            print("         H")
        if o==9:
            print("         I")
        if o==10:
            print("         J")
        if o==11:
            print("         K")
        if o==12:
            print("         L")
        if o==13:
            print("         M")
        if o==14:
            print("         N")
        if o==15:
            print("         O")
        if o==16:
            print("         P")
        if o==17:
            print("         Q")
        if o==18:
            print("         R")
        if o==19:
            print("         S")
        if o==20:
            print("         T")
        if o==21:
            print("         U")
        if o==22:
            print("         V")
        if o==23:
            print("         W")
        if o==24:
            print("         X")
        if o==25:
            print("         Y")
        if o==26:
            print("         Z")

        time.sleep(2)

        if l==1:
            print("         A")
        if l==2:
            print("         B")
        if l==3:
            print("         C")
        if l==4:
            print("         D")
        if l==5:
            print("         E")
        if l==6:
            print("         F")
        if l==7:
            print("         G")
        if l==8:
            print("         H")
        if l==9:
            print("         I")
        if l==10:
            print("         J")
        if l==11:
            print("         K")
        if l==12:
            print("         L")
        if l==13:
            print("         M")
        if l==14:
            print("         N")
        if l==15:
            print("         O")
        if l==16:
            print("         P")
        if l==17:
            print("         Q")
        if l==18:
            print("         R")
        if l==19:
            print("         S")
        if l==20:
            print("         T")
        if l==21:
            print("         U")
        if l==22:
            print("         V")
        if l==23:
            print("         W")
        if l==24:
            print("         X")
        if l==25:
            print("         Y")
        if l==26:
            print("         Z")

        time.sleep(2)

        if c==1:
            print("         A")
        if c==2:
            print("         B")
        if c==3:
            print("         C")
        if c==4:
            print("         D")
        if c==5:
            print("         E")
        if c==6:
            print("         F")
        if c==7:
            print("         G")
        if c==8:
            print("         H")
        if c==9:
            print("         I")
        if c==10:
            print("         J")
        if c==11:
            print("         K")
        if c==12:
            print("         L")
        if c==13:
            print("         M")
        if c==14:
            print("         N")
        if c==15:
            print("         O")
        if c==16:
            print("         P")
        if c==17:
            print("         Q")
        if c==18:
            print("         R")
        if c==19:
            print("         S")
        if c==20:
            print("         T")
        if c==21:
            print("         U")
        if c==22:
            print("         V")
        if c==23:
            print("         W")
        if c==24:
            print("         X")
        if c==25:
            print("         Y")
        if c==26:
            print("         Z")

        time.sleep(2)


        if a==1:
            print("         A")
        if a==2:
            print("         B")
        if a==3:
            print("         C")
        if a==4:
            print("         D")
        if a==5:
            print("         E")
        if a==6:
            print("         F")
        if a==7:
            print("         G")
        if a==8:
            print("         H")
        if a==9:
            print("         I")
        if a==10:
            print("         J")
        if a==11:
            print("         K")
        if a==12:
            print("         L")
        if a==13:
            print("         M")
        if a==14:
            print("         N")
        if a==15:
            print("         O")
        if a==16:
            print("         P")
        if a==17:
            print("         Q")
        if a==18:
            print("         R")
        if a==19:
            print("         S")
        if a==20:
            print("         T")
        if a==21:
            print("         U")
        if a==22:
            print("         V")
        if a==23:
            print("         W")
        if a==24:
            print("         X")
        if a==25:
            print("         Y")
        if a==26:
            print("         Z")

        time.sleep(2)

        if n==1:
            print("         A")
        if n==2:
            print("         B")
        if n==3:
            print("         C")
        if n==4:
            print("         D")
        if n==5:
            print("         E")
        if n==6:
            print("         F")
        if n==7:
            print("         G")
        if n==8:
            print("         H")
        if n==9:
            print("         I")
        if n==10:
            print("         J")
        if n==11:
            print("         K")
        if n==12:
            print("         L")
        if n==13:
            print("         M")
        if n==14:
            print("         N")
        if n==15:
            print("         O")
        if n==16:
            print("         P")
        if n==17:
            print("         Q")
        if n==18:
            print("         R")
        if n==19:
            print("         S")
        if n==20:
            print("         T")
        if n==21:
            print("         U")
        if n==22:
            print("         V")
        if n==23:
            print("         W")
        if n==24:
            print("         X")
        if n==25:
            print("         Y")
        if n==26:
            print("         Z")                     #Fin de la partie d'affichage des lettres

        print("___________________________________________")

        time.sleep(2)
        print("___________________________________________")
        print("Vérification en cours . . .")
        print("___________________________________________")
        time.sleep(2)

        if v==3:
            print("___________________________________________")
            print("La première lettre est bonne")

        else:
            print("___________________________________________")
            print("La première lettre n'est pas bonne")                         #Dire au joueurs quelles lettres sont bonne ou mauvaise en fonction du mot choisis

        time.sleep(1)
        if o==15:
            print("___________________________________________")
            print("La deuxième lettre est bonne")
        else:
            print("___________________________________________")
            print("La deuxième lettre n'est pas bonne")

        time.sleep(1)
        if l==21:
            print("___________________________________________")
            print("La troisième lettre est bonne")
        else:
            print("___________________________________________")
            print("La troisième lettre n'est pas bonne")

        time.sleep(1)
        if c==16:
            print("___________________________________________")
            print("La quatrième lettre est bonne")
        else:
            print("___________________________________________")
            print("La quatrième lettre n'est pas bonne")

        time.sleep(1)
        if a==5:
            print("___________________________________________")
            print("La cinquième lettre est bonne")
        else:
            print("___________________________________________")
            print("La cinquième lettre n'est pas bonne")

        time.sleep(1)
        if n==18:
            print("___________________________________________")
            print("Le sixième lettre est bonne")
            print("___________________________________________")
        else:
            print("___________________________________________")
            print("La sixième lettre n'est pas bonne")                      #Fin de l'affichage  de l'ordre des lettres
            print("___________________________________________")
        print("     ")
        print("___________________________________________")
        print("Une attente de 2 secondes: Veuillez patientez . . .")
        print("___________________________________________")
        time.sleep(2)
        print("     ")








        if compteur==1:                         #En fonction du nombe de tour perdu, afficher la parti du pendu pour compléter
                                                #Il n'y a que 9 essais
            debut("red")


        if compteur==2:
            b("red")


        if compteur==3:
            dessus("red")

        if compteur==4:
            d("red")

        if compteur==5:
            e("red")

        if compteur==6:
            f("red")

        if compteur==7:
            g("red")

        if compteur==8:
            h("red")

        if compteur==9:
            i("red")
            print("___________________________________________")
            print("      PERDU")            #dire au joueur sa defaite
            print("___________________________________________")
            drapeau=1                       #Sortir alors de la boucle

        if v==3 and o==15 and l==21 and c==16 and a==5 and n==18:       #Condition = Si toute les insertions correspondent au lettre => gagner
            print("___________________________________________")
            print("Gagné")
            print("___________________________________________")
            compteur=10                                                 #Compteur = 10 pour pas activé les futurs partis du pendue
            drapeau=1



tl.mainloop () #laisser ouvert le paneau TURTLE

