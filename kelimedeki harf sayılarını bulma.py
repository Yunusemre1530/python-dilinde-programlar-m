metin= input("kelime giriniz: ")
sozluk= dict()
for harf in metin:
    if harf in sozluk:
        sozluk[harf]+=1
    else:
        sozluk[harf]=1
for harf,adet in sozluk.items():
    print(harf,adet)