#Créé par Enzo Sanchez Valero
#Créé le 31/08/23
#TP2 (jeu de devinette)

import random

nb_ordi=random.randint(0,1000)
nb_essais=0

def jeu():
    print('L`ordinateur a choisi le nombre à deviner')
    nombre=int(input('Choissisez un nombre:'))
    if nombre>nb_ordi:
        print('Le nombre à deviner est plus petit que',nombre,'')
    elif nombre<nb_ordi:
        print('Le nombre à deviner est plus grand que',nombre,'')
jeu()
