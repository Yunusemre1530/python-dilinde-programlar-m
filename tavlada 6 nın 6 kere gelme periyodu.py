from tkinter import W


import random
tavla={1:0,2:0,3:0,4:0,5:0,6:0}
sayac=0
while True:
    tas=random.randint(1,6)
    tavla[tas]+=1
    sayac+=1
    if tavla[6]==6:
        break
print(sayac)