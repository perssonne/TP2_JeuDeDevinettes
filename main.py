

import random

def jeu():
    bornes=str(input('Voulez-vous choisir vous-même l intervalle du nombre à découvrir? (y/n)'))
    if bornes == ('y'):
        borne_minimale=int(input('Quelle sera la borne minimale?'))
        borne_maximale=int(input('Quelle sera la borne maximale?'))
    elif bornes == ('n'):
        borne_minimale=0
        borne_maximale=100
    else:
        print('Erreur')

    chiffre_aléatoire = random.randint(borne_minimale,borne_maximale)
    print(f'L ordinateur a choisi un nombre entre {borne_minimale} et {borne_maximale}.')
    nb_essais=1

    while True:

        essai=int(input("Entrez votre essai:"))

        if essai > chiffre_aléatoire:
            print("Trop grand.")
            nb_essais=nb_essais+1
        elif essai<chiffre_aléatoire:
            print("Trop petit.")
            nb_essais=nb_essais+1
        elif essai==chiffre_aléatoire:
            print("Vous avez réussi en",nb_essais,"essais. Bravo!")
            quit=str(input('Voulez-vous refaire une partie? (y/n)'))
            if quit == ('y'):
                jeu()
            elif quit == ('n'):
                print('Merci et au revoir.')
                break
        else:
            print("Erreur")

print('Bienvenue dans ce jeu de devinette.')
jeu()