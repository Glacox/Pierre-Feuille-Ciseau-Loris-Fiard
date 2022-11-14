# Début
import random as r

# On admet une fonction Key qui detecte sur quelle touche on a appuyé.
# On admet une fonction Random qui choisi aléatoirement un chiffre entre 1 et 3 compris.
# On admet une fonction Input qui récupère ce que le joueur à marqué.


# On crée une constante MenuState type Booléen qu'on initialise comme Fausse
MenuState=False
# On crée une variable ScoreJoueur qu'on initialise à 0
ScoreJoueur=0
# On crée une variable ScoreIA qu'on initialise à 0
ScoreIA=0
# On crée une variable Quit qu'on initialise comme Fausse
Quite=False
# On crée une variable QuitDetect qu'on initialise à 0
QuitDetect=0

# On crée une fonction Joueur avec la variable choixJoueur tel que
def Joueur(choixJoueur):
#     On affiche "Pierre = 1, Feuille = 2, Ciseau = 3"
    print("Pierre = 1, Feuille = 2, Ciseau = 3")
#     On définit la variable choixJoueur avec le retour de l'execution de la fonction Input
    choixJoueur = int(input("test"))

#     On retourne la variable choixJoueur
    return choixJoueur



# On crée une fonction IA avec la variable choixIA tel que
def IA (choixIA) :
#     On définit la variable choixIA avec le retour de l'execution de la fonction Random
    choixIA=r.randint(1,3)
#     Si la variable choixIA est égale à 1 alors 
#         on affiche "L'IA a choisi Pierre"

#     Si la variable choixIA est égale à 2 alors 
#         on affiche "L'IA a choisi Feuille"

#     Si la variable choixIA est égale à 3 alors 
#       on affiche "L'IA a choisi Ciseau"
    
#     On retourne la variable choixIA



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