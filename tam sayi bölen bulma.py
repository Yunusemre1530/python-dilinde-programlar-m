sayi=int(input("bir sayi giriniz "))
sayac=0
for i in range(1,sayi+1):
    if sayi%i==0:
        print(i)
        sayac+=1
print(f"{sayi} sayisinin pozitif tam bölen sayisi {sayac} dir dır")