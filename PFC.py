import random as r

Quit=False
ScoreJoueur=0
ScoreIA=0

def Joueur():
    syntax=False
    while syntax==False:
        choixJoueur = int(input("Pierre = 1, Feuille = 2, Ciseau = 3"))
        if choixJoueur==1:
            syntax=True
        elif choixJoueur==2:
            syntax=True
        elif choixJoueur==3:
            syntax=True
        else:
            print("Je n'ai pas compris")
            
    return choixJoueur
def IA():
    choixIA=r.randint(1,3)
    if choixIA==1:
        print("L'IA a choisi Pierre")
    if choixIA==2:
        print("L'IA a choisi Feuille")
    if choixIA==3:
        print("L'IA a choisi Ciseau")
    return choixIA


def Result():
    choixJoueur = Joueur()
    choixIA = IA()

    if choixJoueur==choixIA:
        print("Egalité !")
    
    elif choixJoueur==1 and choixIA==3:
        print("Le joueur a gagné")

    elif choixJoueur==2 and choixIA==1:
        print("Le joueur a gagné")

    elif choixJoueur==3 and choixIA==2:
        print("Le joueur a gagné")

    elif choixJoueur==1 and choixIA==2:
        print("L'IA a gagné")

    elif choixJoueur==2 and choixIA==3:
        print("L'IA a gagné")

    elif choixJoueur==3 and choixIA==1:
        print("L'IA a gagné")

def Restart():
    global Quit
    print("Voulez-vous rejouer ? 1 = oui, 2 = non")
    QuitDetect = int(input())
    if QuitDetect==1:
        Quit==True
    else:
        Quit==False
    return Quit


while Quit==False:
    Result()
    Restart()