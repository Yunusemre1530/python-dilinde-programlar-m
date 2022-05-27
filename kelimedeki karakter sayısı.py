from re import T


kelime= input("kelime giriniz: ")
toplam=0
i=0
for d in kelime:
    for b in kelime:
        if d==b:
            toplam=toplam+1
    print(f"{kelime} kelimesinde {d} harfi {toplam} tane vardır")
    toplam=0
    