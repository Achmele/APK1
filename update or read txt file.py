import tkinter

def modif():
    way=input("Entrez le nom et l'extension du fichier:")
    doc=open(way,"w")
    modificat=input("Nouveau texte :")
    print(doc.write(str(modificat)))
    print("Texte modifier avec succés. ")
    doc.close()
def lire():  
    
    way=input("Entrez le nom et l'extension du fichier:")
    doc=open(way,"r")
    print("Le texte contenu dans ",way,"est:",doc.read())
    doc.close()
win=tkinter.Tk()
win.geometry("400x150")
win.title("page de modification")
m=tkinter.Label(text=" Souhaitez vous lire ou modifier le fichier..?")
m.pack()
btn1=tkinter.Button(text="modifier..!",command=modif)
btn1.pack()
btn2=tkinter.Button(text="lire..!",command=lire,width=8)
btn2.pack()
btn3=tkinter.Button(text="Annuler ",command=win.quit,width=8)
btn3.pack()
win.mainloop()