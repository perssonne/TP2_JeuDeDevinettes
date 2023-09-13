

import random

def boucle_jeu():
    chiffre_aléatoire = random.randint(0,1000)
    print("L'ordinateur a choisi un nombre entre 0 et 1000.")
    while boucle_jeu=False:
        essai=str(int("Entrez votre essai:"))
        if essai>chiffre_aléatoire:
            print("Trop grand.")
            nb_essais=nb_essais+1
        elif essai<chiffre_aléatoire:
            print("Trop petit.")
            nb_essais=nb_essais+1
        elif essai==chiffre_aléatoire:
            print("Vous avez réussi en",nb_essais," essais. Bravo!")
            boucle_jeu = True
        else:
            print("Erreur")

boucle_jeu()

