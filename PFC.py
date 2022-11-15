import random as r

MenuState=False
ScoreJoueur=0
ScoreIA=0
Quite=False
QuitDetect=0

def Joueur(choixJoueur):
    print("Pierre = 1, Feuille = 2, Ciseau = 3")
    choixJoueur = int(input("test"))
    return choixJoueur

def IA (choixIA) :
    choixIA=r.randint(1,3)
    if choixIA==1:
        print("L'IA a choisi Pierre")
    if choixIA==2:
        print("L'IA a choisi Feuille")
    if choixIA==3:
        print("L'IA a choisi Ciseau")
    return choixIA



# On crée une fonction Result telle que
    
#     Si la variable choixJoueur est égale variable choixIA alors 
#         on affiche "Egalité !"

#     Ou si la variable choixJoueur est égale à 1 et que la variable choixIA est égale à 3 alors 
#         on affiche "Le joueur a gagné"
#         on ajoute 1 à ScoreJoueur

#     Ou si la variable choixJoueur est égale à 2 et que la variable choixIA est égale à 1 alors 
#         on affiche "Le joueur a gagné"
#         on ajoute 1 à ScoreJoueur

#     Ou si la variable choixJoueur est égale à 3 et que la variable choixIA est égale à 2 alors 
#         on affiche "Le joueur a gagné"
#         on ajoute 1 à ScoreJoueur

#     Ou si la variable choixJoueur est égale à 1 et que la variable choixIA est égale à 2 alors 
#         on affiche "Le joueur a perdu"
#         on ajoute 1 à ScoreIA

#     Ou si la variable choixJoueur est égale à 2 et que la variable choixIA est égale à 3 alors 
#         on affiche "Le joueur a perdu"
#         on ajoute 1 à ScoreIA

#     Ou si la variable choixJoueur est égale à 3 et que la variable choixIA est égale à 1 alors 
#         on affiche "Le joueur a perdu"
#         on ajoute 1 à ScoreIA

# On crée une fonction Restart telle que
#     On affiche "Voulez-vous rejouer ? 1 = oui, 2 = non"
#     On définit la variable QuitDetect entrée par l'utilisateur avec la fonction Input
    
#     Si QuitDetect est égale à 1 alors
#         On attribue la valeur Vraie à Quit
#     Sinon
#         On attribue la valeur Fausse à Quit


# Tant que Quit est Fausse alors

#     Tant que MenuState est Fausse alors

#         On affiche "Appuyer sur Entrée pour commencer"
        
#         Si la touche "Entrée" est detectée par la fonction Key alors
#             Définir MenuState comme Vraie
        
#         On retourne la variable Menustate


#     Tant que ScoreJoueur est strictement inférieur à 3 ou que ScoreIA est strictement inférieur à 3 alors
#         On execute la fonction Joueur
#         On execute la fonction IA
#         On execute la fonction Result
    
#     On appelle la fonction Restart


# FIN