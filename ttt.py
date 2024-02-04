import tkinter
from tkinter import messagebox
import time
import random
from random import randrange
"""     
win1=tkinter.Tk()
bg="azure"
win1.config(background=bg)
win1.title("Page d'acceui..")
message1=tkinter.Label(text="Bienvenue !!!!",font=40)
message1.pack()
message2=tkinter.Label(text="Avez vous deja un compte joueur ???",font=10,background=bg,)
message2.pack()
entry1=tkinter.Entry(bg="darkgray")
entry1.pack()
btn1=tkinter.Button(text="Soumettre",font=20,width=15,background=bg,fg="light green",command=win1.quit)
btn1.pack()
win1.geometry("500x500")
win1.mainloop()
print(entry1.get())"""

"""
win2=tkinter.Tk()

win2.geometry("500x500")
win2.title("Page de connection...")
win2.config(background=bg)
title=tkinter.Label(text="Page de connection",font=50)
user_label=tkinter.Label(text="Nom d'utilisteur :")
user_entry=tkinter.Entry()
password_label=tkinter.Label(text="Mot de passe:")
password_entry=tkinter.Entry()
btn2=tkinter.Button(text="Soumettre",font=20,width=15,background=bg,fg="light green",command=win2.quit)
    
user_label.pack()
user_entry.pack()
password_label.pack()
password_entry.pack()
btn2.grid()
win2.mainloop()
def oui():
    a="oui"
    print(str(a))
    
def non():
    messagebox.showwarning("warning","fred")
    a="non"
    print(str(a))
win=tkinter.Tk(bg=7, 43, 3))
entry=tkinter.Entry()
entry.pack()
btn=tkinter.Button(text="oik",command=win.quit)
r1=tkinter.Checkbutton(text="oui",command=oui)
r2=tkinter.Checkbutton(text="non",)
r2.config()
r1.pack()
r2.pack()
btn.pack()
win.mainloop()
me=tkinter.Tk()
me.geometry("400x400")
a=True
while a==True:
            
       messa=tkinter.Label(text=".")
       messa.pack()
       
       time.sleep(2)
       
       me.mainloop()
       
       messa.destroy()
       messa=tkinter.Label(text="..")
       messa.pack()
       me.mainloop()
       time.sleep(2)
       
        
       messa=tkinter.Label(text="...")
       messa.pack()
       me.mainloop()
       time.sleep(2)
       messa.destroy()
       
o=tkinter.Tk()
s=tkinter.Entry()
s.pack()
a=tkinter.Button(text="ok",command=o.quit)
a.pack()
x=str(s.get())


if int(s.get())<0:
    print("negatif")
elif int(s.get())>0:
    print("positif")
o.mainloop()
one=tkinter.Tk()
one.geometry("400x400")
mess=tkinter.Label(text="txt")
mess.pack()
btn=tkinter.Button(text="ok",command=one.quit)
btn.pack()
one.mainloop()

import hashlib
from hashlib import sha256   
    
chemin ="comptes/du bois" 
sortie = "comptes/Data subtitutions"
keys = sha256(("du bois").encode("utf_8")).digest()
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
def name ():
    m1=tkinter.Label(text="KOUNOU")
    m1.pack()
    win.mainloop()
    m1.destroy()
def prenom():
    m2=tkinter.Label(text="Fred")
    m2.pack()
    win.mainloop()
    m2.destroy()
def age ():
    
    m3=tkinter.Label(text="18 ans")
    m3.pack()
    win.mainloop()
    btn=tkinter
    


win=tkinter.Tk()
win.geometry("400x400")
mainmenu=tkinter.Menu()
principal=tkinter.Menu()
m1=tkinter.Label(text="Salut tous")
m1.pack()
principal.add_command(label="name",command=name)
principal.add_command(label="premon",command=prenom)
second=tkinter.Menu()
mainmenu.add_cascade(label="description de fred",menu=principal)
win.config(menu=mainmenu)
win.mainloop()

with open("comptes/"+ "sss","w") as fichier:
            fichier.write(str("\n"))
            fichier.write(str(1000)+("oui"))
with open("comptes/" + "sss", "a") as fichier:
            fichier.write(str("\n"))
            fichier.write(str("password"+"oui"))  
with open("comptes/" + "sss", "a") as fichier:
         
         fichier.write(str("red"+"oui"))
         time.sleep(0.5)
with open("comptes/" + "sss", "r") as fichier:
    print(fichier.read())
    
    
win=tkinter.Tk()
win.geometry("400x400")
mainmenu=tkinter.Menu()
mainmenu.add_command(label="affichage")
mainmenu.add_command(label="Mon compte")
smenu=mainmenu.add_command(label="ok")
smenu.add_command(label="oui", menu=mainmenu)
smenu.add_command(label="non", menu=mainmenu)


win.config(menu=mainmenu,bg="aquamarine")
win.mainloop()"""
