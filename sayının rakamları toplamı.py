#sayi= int(input("bir sayi giriniz: "))
#toplam=0
#geçicisayi=sayi
#while geçicisayi>0:
#    b=geçicisayi%10
#    toplam+=b
#    geçicisayi//=10
#print(f"{sayi} sayısının rakamları toplamı {toplam} dir dır")
#string li hali aşağıda
sayi=int(input("bir sayi giriniz: "))
sayi_str=str(sayi)
toplam=0
for i in sayi_str:
    toplam+=int(i)
print(toplam)
