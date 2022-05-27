sayi= int(input("bir sayi girriniz 6"))
faktoriyel=1
#while sayi>=1:
#    faktoriyel*=sayi
#    sayi-=1
#print(faktoriyel)
for i in range(1,sayi+1):
    faktoriyel*=i
print(faktoriyel)
