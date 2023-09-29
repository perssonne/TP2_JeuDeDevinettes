#Créé par Enzo Sanchez Valero
#Créé le 31/08/23
#TP2 (jeu de devinette)

import random


def jeu():      #Définir la fonction

    bornes=str(input('Voulez-vous choisir vous-même l intervalle du nombre à deviner? (y/n)'))      #Définition des bornes

    if bornes == ('y'):     #Bornes personnalisées
        borne_minimale=int(input('Quelle sera la borne minimale?'))
        borne_maximale=int(input('Quelle sera la borne maximale?'))
    elif bornes == ('n'):   #Bornes par défaut
        borne_minimale=0
        borne_maximale=100
    else:
        print('Erreur')     #En cas d'erreur il faut relancer le jeu

    chiffre_aléatoire = random.randint(borne_minimale,borne_maximale)       #Choix du nombre a deviner
    print(f"L'ordinateur a choisi un nombre entre {borne_minimale} et {borne_maximale}.")
    nb_essais=1     #Nombre d'essais ajusté

    while True:     #Boucle while

        essai = int(input("Entrez votre essai:"))

        if essai > chiffre_aléatoire:
            print("Trop grand.")
            nb_essais=nb_essais+1
        elif essai < chiffre_aléatoire:
            print("Trop petit.")
            nb_essais=nb_essais+1
        elif essai==chiffre_aléatoire:      #Nombre trouvé!
            print("Vous avez réussi en",nb_essais,"essais. Bravo!")
            quit=str(input('Voulez-vous refaire une partie? (y/n)'))        #Rejouer (yes/no)
            if quit == ('y'):       #Nouvelle partie
                jeu()
            elif quit == ('n'):     #Fin du jeu
                print('Merci et au revoir.')
                break       #Fin de la boucle
        else:       #En cas d'erreur la boucle continue
            print("Erreur")


print('Bienvenue dans ce jeu de devinette.')        #Phrase d'accueil

jeu()       #Début de la fonction
