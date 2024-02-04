import time
import random
import tkinter
from tkinter import messagebox
from random import randrange
somme = 1000
z=13
print("")
time.sleep(1)
print("La parti prend fin lorsque votre solde est vide ou insuffisant pour lancer une nouvelle parti ")
time.sleep(3)
print("Bienvenue au joueur !!!")
time.sleep(2)
#Debut boucle principale....
while z==13:
    mise = int()
    chiffre_var =randrange(2)
    new_somme = int()
    print("")
    print("Vous disposer a présent de", somme, " fcfa")
    print("")
    time.sleep(2)
    y=1
    #Debut boucle concernant le chiffre choisi.....
    while y==1:
            print("Vous devez choisir un chiffre compris entre 0 et 2")
            time.sleep(2)
            print("")
            chiffre = input("Entrez le chiffre sur le quel vous souhaitez miser:")
            time.sleep(1)
            print("")
            if  0<int(chiffre)>2 or int(chiffre)<0:
                print("Une erreur est survenu !!!!")
                time.sleep(1)
                
            else:
                y=2
    u=1
    #Début de la boucle concernant la mise.....
    while u==1:
        mise = input("Combien voullez miser:")
        if int(mise)>int(somme) :
            time.sleep(1)
            print("Une erreur est survenu !!!!")
            time.sleep(1)
            print("")
            print("Votre solde est  inssuffisant !")
            print("")
            time.sleep(1)
            
        elif int(mise)<=99:
            time.sleep(1)
            print("Une erreur est survenu !!!!")
            time.sleep(1)
            print("La mise doit être superieur ou egale a 100 fcfa")
            print("")
            time.sleep(1)
        else:
            u=2  
#suite de prgmm
    time.sleep(1)
    print("")
    print("Vous avez miser:", mise, " fcfa sur le chiffre:",chiffre)
    print("")
    time.sleep(1)
    somme_after_mise=int()
    somme_after_mise= int(somme) - int(mise)
    print("Il vous reste dans votre solde:",somme_after_mise," fcfa")
    time.sleep(2)
    print("")
    print("la roue tourne ,patientez....")
    print("")
    print("3")
    time.sleep(1)
    print("")
    print("2")
    time.sleep(1)
    print("")
    print("1")
    print("")
    time.sleep(1)
    print("Le chiffre gagnant est: ", chiffre_var)
    time.sleep(2)
    print("Et vous avez choisi le chiffre:",chiffre)
    time.sleep(2)
    #En cas de gain......
    if int(chiffre) == int(chiffre_var):
        gain=( (1) * int(mise))
        new_somme =   int(gain) + int(somme)
        print("")
        print("Gagner!")
        print("")
        time.sleep(1)
        print("Félicitation !,vous avez deviner le chiffre gagnant.")
        print("")
        time.sleep(2)
        print("Les", mise, "  fcfa misées  vienne donc de doubler !!!")
        print("")
        time.sleep(2)
        print("Vous venez de gagner ",gain," fcfa")
        print("")
        time.sleep(2)
        print("Vous avez à présent ", new_somme, " fcfa sur votre compte")
    else:
#En cas de perte....
        new_somme = int(somme) - int(mise)
        print("")
        print("Perdu !")
        print("")
        time.sleep(1)
        print("Vous n'avez malheuresement pas deviner le nombre gagnant :(")
        print("")
        time.sleep(2)
        print("Les",mise, " fcfa misées sont donc definitivement retirer de votre compte.")
        print("")
        time.sleep(2)
        print("Vous avez a présent ", new_somme, " fcfa sur votre compte")
        print("")
#pour actualiser le solde j'ai fait....
    somme = new_somme  
    #Concernant le solde vide ....
    if int(somme)==0:
        z=12
        print("Votre solde est totalement vide .")
        print("")
        time.sleep(1)
        print("La partie prend fin pour vous")
        time.sleep(1)
        print("Merci d'avoir jouer.")
        print("")
        time.sleep(1)
        print("Au plaisir de vite vous retrouvé")
#concernant le solde insuffissant ....  
    else:
         if int(somme)<=99:
            time.sleep(1)
            print("Votre solde actuel est inssuffisant pour lancer une nouvelle partie.")
            time.sleep(2)
            print("")
            print("La parti prend automatiquement fin..")
            print("")
            time.sleep(2)
            print("Merci d'avoir jouer.")
            print("")
            time.sleep(2)
            print("Au plaisir de vite vous retrouvé")
            z=12
         if z==12:
             z=12
         else: 
            x=1
#Suite du jeu...
            while x==1:
                time.sleep(1)
                play = input("Continuer as jouer ? oui ou non:")
                print("")
            
                if play=="oui":
                    print("Le jeu continu....")
                    print("")
                    time.sleep(2)
                    x=2
        
                elif play=="non":
                    print("Vous quitter le jeu...avec une solde de ",somme," fcfa")
                    print("")
                    time.sleep(2)
                    print("Faite rapidement le retrait de vos gains")
                    print("")
                    time.sleep(2)
                    print("Au plaisir de vite vous retrouvé")
                    print("")
                    time.sleep(1)
                    print("Fin du jeu..")
                    x=2
                    z=12
                else:
                    time.sleep(1)