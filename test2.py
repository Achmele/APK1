import tkinter
from tkinter import *
win=tkinter.Tk()
win.geometry("400x150")
win.title("Syncronisation")
mainmenu=tkinter.Menu()
menu1=tkinter.Menu(mainmenu)
menu1.add_command(label="vivre")
menu1.add_command(label="shiner")
mainmenu.add_cascade(label="opt",menu=menu1)
win.config(menu=mainmenu)
tof=tkinter.PhotoImage(file='mon_logo2.png')
mess=Label(win,image=tof)
mess.place(x='-500',y='-500')

win.mainloop()