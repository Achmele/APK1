import tkinter

def valide():
    t = message.get()
    
    pass
"""
wins = tkinter.Tk()
wins.title(11111)
wins.geometry("400x400")
message = tkinter.Entry(wins)
t = message.get()
btn = tkinter.Button(wins, text="ok",command=wins.quit)
message.pack()
btn.pack()
wins.mainloop()
print(str(message.get()))"""

a=0
while a==0:
        win = tkinter.Tk()
        win.title(22222)
        win.geometry("400x400")
        message = tkinter.Entry(win)
        t = message.get()
        btn = tkinter.Button(win, text="ok", command=win.quit)
        
        message.pack()
        btn.pack()
        win.mainloop()
        if message.get()== "r":
           pass
        
        elif message.get()== "q":
                a=1