print("Algoritme des nombres premiers")
n=0
i=0
c=0

n=input("Entrez le nombre a evaluer :")
 
if n==1:
    print("1 n'est pas un nombre premier")
elif n!=0:
    for i in range (2, int(n)):
       
        if  int(n)% i ==0:
         c=c+1
    
if c==0 :
      print(str(n)+ " est un nombre premier")
else : 
    print(str(n) +"  n'est pas un nombre premier")