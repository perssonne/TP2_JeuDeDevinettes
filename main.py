

import random

chiffre_aléatoire = random.randint(0,1000)
print("L'ordinateur a choisi un nombre entre 0 et 1000.")
nb_essais=0
boucle_jeu=True
while boucle_jeu:
    essai=int(input("Entrez votre essai:"))
    if essai > chiffre_aléatoire:
        print("Trop grand.")
        nb_essais=nb_essais+1
        boucle_jeu = True
    elif essai<chiffre_aléatoire:
        print("Trop petit.")
        nb_essais=nb_essais+1
        boucle_jeu = True
    elif essai==chiffre_aléatoire:
        print("Vous avez réussi en",nb_essais,"essais. Bravo!")
        print()
        boucle_jeu = False
    else:
        print("Erreur")
        boucle_jeu = True

rejouer=str(input('Voulez vous rejouer oui ou non?'))
