#Créé par Enzo Sanchez Valero
#Créé le 31/08/23
#TP2 (jeu de devinette)

import random

# Définir la fonction
def jeu():

    # Définition des bornes
    bornes=str(input('Voulez-vous choisir vous-même l intervalle du nombre à deviner? (y/n)'))

    # Bornes personnalisées
    if bornes == ('y'):
        borne_minimale=int(input('Quelle sera la borne minimale?'))
        borne_maximale=int(input('Quelle sera la borne maximale?'))

    # Bornes par défaut
    elif bornes == ('n'):
        borne_minimale=0
        borne_maximale=100

    # En cas d'erreur il faut relancer le jeu
    else:
        print('Erreur')

    # Choix du nombre a deviner
    chiffre_aléatoire = random.randint(borne_minimale,borne_maximale)
    print(f"L'ordinateur a choisi un nombre entre {borne_minimale} et {borne_maximale}.")
    # Nombre d'essais ajusté
    nb_essais = 1

    while True:
        essai = int(input("Entrez votre essai:"))

        if essai > chiffre_aléatoire:
            print("Trop grand.")
            nb_essais = nb_essais + 1
        elif essai < chiffre_aléatoire:
            print("Trop petit.")
            nb_essais = nb_essais + 1
        # Nombre trouvé!
        elif essai == chiffre_aléatoire:
            print("Vous avez réussi en", nb_essais, "essais. Bravo!")
            # Rejouer (yes/no)
            quit = str(input('Voulez-vous refaire une partie? (y/n)'))
            # Nouvelle partie
            if quit == ('y'):
                jeu()
                break
            # Fin du jeu
            elif quit == ('n'):
                print('Merci et au revoir.')
                False
                # Fin de la boucle
                break

        # En cas d'erreur la boucle continue
        else:
            print("Erreur")


# Phrase d'accueil
print('Bienvenue dans ce jeu de devinette.')

# Début de la fonction
jeu()