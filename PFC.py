import random as r

ScoreJoueur=0
ScoreIA=0
Quit=False
QuitDetect=0

def Joueur():
    print("Pierre = 1, Feuille = 2, Ciseau = 3")
    choixJoueur = int(input())
    return choixJoueur
def IA() :
    choixIA=r.randint(1,3)
    if choixIA==1:
        print("L'IA a choisi Pierre")
    if choixIA==2:
        print("L'IA a choisi Feuille")
    if choixIA==3:
        print("L'IA a choisi Ciseau")
    return choixIA


def Result():
    global ScoreIA
    global ScoreJoueur
    choixJoueur=Joueur()
    choixIA=IA()
    
    if choixJoueur==choixIA:
        print("Egalité !")
    
    elif choixJoueur==1 and choixIA==3:
        print("Le joueur a gagné")
        ScoreJoueur+=1

    elif choixJoueur==2 and choixIA==1:
        print("Le joueur a gagné")
        ScoreJoueur+=1

    elif choixJoueur==3 and choixIA==2:
        print("Le joueur a gagné")
        ScoreJoueur+=1

    elif choixJoueur==1 and choixIA==2:
        print("L'IA a gagné")
        ScoreIA+=1

    elif choixJoueur==2 and choixIA==3:
        print("L'IA a gagné")
        ScoreIA+=1

    elif choixJoueur==3 and choixIA==1:
        print("L'IA a gagné")
        ScoreIA+=1

def Restart():
    print("Voulez-vous rejouer ? 1 = oui, 2 = non")
    QuitDetect = int(input())
    if QuitDetect==1:
        Quit==True
    else:
        Quit==False
    
while Quit==False:
    while ScoreJoueur<3 or ScoreIA<3:
        Joueur()
        IA()
        Result()
        Restart()