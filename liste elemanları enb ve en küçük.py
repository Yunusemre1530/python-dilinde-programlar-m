terim=int(input("kac sayi girilecek: "))
liste= []
for i in range(1,terim+1):
    sayi=int(input(f"{i}.sayiyi giriniz: "))
    liste.append(sayi)
print(f"listedeki en büyük sayi {max(liste)} en küçük sayi {min(liste)}")