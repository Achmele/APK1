import time
import random
from random import randrange
somme = 1000
while somme > 0:
    print("Bienvenue au joueur !!!")
    time.sleep(1)

    mise = int()
    chiffre_var = randrange(2)
    new_somme = int()
    print("")
    print("Vous disposer de", somme, "fcfa")
    print("")
    time.sleep(1)

    print("Choisisez un chiffre entre 0 et 2")
    time.sleep(1)
    print("")
    chiffre = input("Entrez le chiffre sur le quel vous souhaitez miser:")
    print("")
    if int(chiffre)>int(chiffre_var):
        print("Vous devez choisir un chiffre en 0 et 2 !")
        print("")
        chiffre = input("Entrez le chiffre sur le quel vous souhaitez miser:")
    mise = input("Combien voullez miser:")
    if int(mise)>int(somme):
        print("une erreur est survenu")
        time.sleep(1)
        print("Solde inssuffisant !")
        mise = input("Combien voullez miser:")
    elif int(mise)<=99:
        print("La mise doit être superieur ou egale a 100fcfa")
        time.sleep(1)
        mise = input("Combien voullez miser:")
    print("")
    print("Vous avez miser:", mise, " fcfa")
    print("")
    print("la roue tourne ,patientez....")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("Le chiffre gagnant est: ", chiffre_var)
    time.sleep(2)

    if int(chiffre) == int(chiffre_var):
        new_somme = (2 * int(mise)) + int(somme)
        print("Gagner!")
        time.sleep(1)
        print("")
        print("Félicitation !,vous avez deviner le chiffre gagnant.")
        print("")
        time.sleep(1)
        print("Les", mise, " fcfa misées  vienne donc de doubler !!!")
        print("")
        print("Vous avez à présent ", new_somme, "fcaf sur votre compte")
    else:
        new_somme = int(somme) - int(mise)
        print("Perdu !")
        time.sleep(1)
        print("")
        print("Vous n'avez malheuresement pas deviner le nombre gagnant :(")
        print("")
        time.sleep(1)
        print(mise, "fcaf est donc retirer de votre compte.")
        print("")
        time.sleep(1)
        print("Vous avez a présent ", new_somme, "fcfa sur votre compte")
        print("")

    somme = new_somme  
    if int(somme)==0:
        print("Votre solde est totalement vide .")
        time.sleep(1)
        print("")
        print("La partie prend fin pour vous")
        time.sleep(1)
        print("Merci d'avoir jouer.")
        print("")
        time.sleep(1)
        print("Au plaisir de vite vous retrouvé")
    else:
    
         play = input("Continuer as jouer ? oui ou non:")
         print("")
         if play=="oui":
           print("Le jeu continu.")
      
         elif play=="non":
            print("Vous quitter le jeu...avec une solde de ",somme)
            time.sleep(1)
            print("")
            print("Faite rapidement le retrait de vos gains")
            time.sleep(1)
            print("")
            print("Au plaisir de vite vous retrouvé")
            somme=0