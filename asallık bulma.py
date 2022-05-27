sayi= int(input("bir sayi giriniz"))
sayac=0
for i in range (2,sayi-1):
    if sayi%i==0:
        print(f"{sayi} asal değildir")
        sayac=0
        break
    else:
     sayac+=1
if sayac !=0:
    print(f"{sayi} asaldir")