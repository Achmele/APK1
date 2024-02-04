import time
import threading
from threading import Thread
def compte ():
    MDP="Akuma"
    while MDP=="Akuma":
    
       
     print(time.strftime("%H"),":",time.strftime("%M"),":", time.strftime("%S"))
     time.sleep(1)
def signal():
     dd=time.strftime("%S")
     while int(dd)==59:
         print("une minute s'est écoulée")

f1=threading.Thread(target=compte())
f2=threading.Thread(target=signal())
f1.start()
f2.start()
f1.join()
f2.join()