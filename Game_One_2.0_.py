import time
import random
import tkinter
import hashlib
from hashlib import sha256
from tkinter import messagebox
from random import randrange

def secure():
        chemin = "comptes/" + name
        sortie = "comptes/Data subtitutions"
        keys = sha256(name.encode("utf_8")).digest()
        with open(chemin, "rb") as f_input:
          with open(sortie, "wb") as f_output:
            a = 0
            while f_input.peek():
                b = ord(f_input.read(1))
                c = a % len(keys)
                d = bytes([b ^ keys[c]])
                f_output.write(d)
                a = a + 1

        with open(sortie, "rb") as f_output:
          data = f_output.read()
          with open(chemin, "wb") as f_input:
            f_input.write(data)
            with open(sortie, "rb") as f_output:
                pass
ae = True
while ae == True:
    state = input("Avez vous deja un compte joueur ??? oui/non:")
    if state == "oui" or state == "non":
        ae = False
    else:
        pass

if state == "non":
    print("Trés bien vous allez donc crée un compte joueur...")
    name = input("Choix du nom d'utilisateur:")
    print(
        "Voila vous avez dés a présent un compte,vous avez par défaut 1000 fcfa  sur votre compte"
    )
    with open("comptes/"+str(name),"w") as fichier:
        fichier.write(str(1000))
    password = input("Choisissez un mot de passe pour votre compte:")
    with open("comptes/" + name, "a") as fichier:
        fichier.write(str("\n" + password))
        time.sleep(0.5)
    secure()

elif state == "oui":
    pass

az = 0
while az == 0:
    name = input("Nom d'utilisateur:")
    try:
        with open("comptes/" + name, "r") as fichier:
            az = 1
    except:
        print("Compte introuvable réessayer..")
ar = True
while ar == True:
    password = input("Entrer le mot de passe:")
    secure()
    with open("comptes/" + name, "r") as fichier:
        lines = fichier.readlines()
        if password != lines[1]:
            ar == True
        elif password == lines[1]:
            ar = False
    secure()
    somme = lines[0]
    time.sleep(0.5)
print("Bienvenu", name, "bonne chance !!!")
z = 13
print("")
time.sleep(1)
print(
    "La parti prend fin lorsque votre solde est vide ou insuffisant pour lancer une nouvelle parti "
)

time.sleep(2)
# Debut boucle principale....
while z == 13:
    mise = int()
    chiffre_var =randrange(3)
    new_somme = int()
    print("")
    print("Vous disposer a présent de", somme, " fcfa")
    print("")
    time.sleep(2)
    y = 1
    # Debut boucle concernant le chiffre choisi.....
    while y == 1:
        print("Vous devez choisir un chiffre compris entre 0 et 2")
        time.sleep(2)
        print("")
        chiffre = input("Entrez le chiffre sur le quel vous souhaitez miser:")
        time.sleep(1)
        print("")
        if 0 < int(chiffre) > 2 or int(chiffre) < 0:
            print("Une erreur est survenu !!!!")
            time.sleep(1)

        else:
            y = 2
    u = 1
    # Début de la boucle concernant la mise.....
    while u == 1:
        mise = input("Combien voullez miser:")
        if int(mise) > int(somme):
            time.sleep(1)
            print("Une erreur est survenu !!!!")
            time.sleep(1)
            print("")
            print("Votre solde est  inssuffisant !")
            print("")
            time.sleep(1)

        elif int(mise) <= 99:
            time.sleep(1)
            print("Une erreur est survenu !!!!")
            time.sleep(1)
            print("La mise doit être superieur ou egale a 100 fcfa")
            print("")
            time.sleep(1)
        else:
            u = 2
    # suite de prgmm
    time.sleep(1)
    print("")
    print("Vous avez miser:", mise, " fcfa sur le chiffre:", chiffre)
    print("")
    time.sleep(1)
    somme_after_mise = int()
    somme_after_mise = int(somme) - int(mise)
    print("Il vous reste dans votre solde:", somme_after_mise, " fcfa")
    time.sleep(2)
    print("")
    print("la roue tourne ,patientez....")
    print("")
    print("...")
    time.sleep(1)
    print("")
    print("..")
    time.sleep(1)
    print("")
    print(".")
    print("")
    time.sleep(1)
    print("Le chiffre gagnant est: ", chiffre_var)
    time.sleep(2)
    print("Et vous avez choisi le chiffre:", chiffre)
    time.sleep(2)
    # En cas de gain......
    if int(chiffre) == int(chiffre_var):
        gain = int(mise)
        new_somme = int(gain) + int(somme)
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
        print("Vous venez de gagner ", gain, " fcfa")
        print("")
        time.sleep(2)
        print("Vous avez à présent ", new_somme, " fcfa sur votre compte")
        with open("comptes/" + name, "w") as fichier:
            fichier.write(str(new_somme))
            fichier.write(str("\n" + password))
            time.sleep(0.5)
        secure()
    else:
        # En cas de perte....
        new_somme = int(somme) - int(mise)
        print("")
        print("Perdu !")
        print("")
        time.sleep(1)
        print("Vous n'avez malheuresement pas deviner le nombre gagnant :(")
        print("")
        time.sleep(2)
        print(
            "Les",
            mise,
            " fcfa misées sont donc definitivement retirer de votre compte.",
        )
        print("")
        time.sleep(2)
        print("Vous avez a présent ", new_somme, " fcfa sur votre compte")
        with open("comptes/" + name, "w") as fichier:
            fichier.write(str(new_somme))
            fichier.write(str("\n" + password))
            time.sleep(0.5)
        secure()
    # pour actualiser le solde j'ai fait....
    somme = new_somme
    # Concernant le solde vide ....
    if int(somme) == 0:
        z = 12
        print("Votre solde est totalement vide .")
        print("")
        time.sleep(1)
        print("La partie prend fin pour vous")
        time.sleep(1)
        print("Merci d'avoir jouer.")
        print("")
        time.sleep(1)
        print("Au plaisir de vite vous retrouvé")
        with open("comptes/" + name, "w") as fichier:
            fichier.write(str(somme))
            fichier.write(str("\n" + password))
        secure()

    # concernant le solde insuffissant ....
    else:
        if int(somme) <= 99:
            time.sleep(1)
            print(
                "Votre solde actuel est inssuffisant pour lancer une nouvelle partie."
            )
            time.sleep(2)
            print("")
            print("La parti prend automatiquement fin..")
            print("")
            time.sleep(2)
            print("Merci d'avoir jouer.")
            print("")
            time.sleep(2)
            print("Au plaisir de vite vous retrouvé")
            with open("comptes/" + name, "w") as fichier:
                fichier.write(str(somme))
                fichier.write(str("\n" + password))
                time.sleep(0.5)
            secure()
            z = 12
        if z == 12:
            z = 12
        else:
            x = 1
            # Suite du jeu...
            while x == 1:
                time.sleep(1)
                play = input("Continuer as jouer ? oui ou non:")
                print("")

                if play == "oui":
                    print("Le jeu continu....")
                    print("")
                    time.sleep(2)
                    x = 2

                elif play == "non":
                    print("Vous quitter le jeu...avec une solde de ", somme, " fcfa")
                    print("")
                    time.sleep(2)
                    print("Faite rapidement le retrait de vos gains")
                    print("")
                    time.sleep(2)
                    print("Au plaisir de vite vous retrouvé")
                    print("")
                    time.sleep(1)
                    print("Fin du jeu..")
                    with open("comptes/" + name, "w") as fichier:
                        fichier.write(str(somme))
                        fichier.write(str("\n" + password))
                        time.sleep(0.5)
                    secure()
                    x = 2
                    z = 12
                else:
                    time.sleep(1)