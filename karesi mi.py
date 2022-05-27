sayi=int(input("Bir sayi girini: "))
prime=True
for i in range (0,150):
    if i*i==sayi:
        prime=False
        print(f"{sayi} {i} sayısının karesidir")
if prime==True:
    print(f"{sayi} hiçbir sayının karesi değildir") 