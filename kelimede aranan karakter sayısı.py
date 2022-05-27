kelime= input("kelimeyi giriniz ")
harf= input("harfi giriniz ")
adet=0
for d in kelime:
    if d==harf:
        adet+=1
print(f"{kelime} kelimesinde {harf} {adet} adet vardır")