#def bilgi_ver(ad):
#    print("merhaba " + ad)
#bilgi_ver("yunus")
#def topla(x,y):
#    print(f"x+y= {x+y}") 
#topla(3,1)
#def ortalama_hesapla(a):
#    toplam=sum(a)
#    adet=len(a)
#    ortalama=toplam/adet
#    print(f"girilen sayıların ortalamaı={ortalama}")
#ortalama_hesapla([1,2,89,67,28,129])
#def buyuk_harfecevir(kelime):
#    kelime=kelime.upper()
#    print(kelime)
#buyuk_harfecevir("yunus")
def indirimli_fiyat(fiyat,yuzde=20):
    indirim=fiyat*(yuzde/100)
    fiyat=fiyat-indirim
    print(f"indirimli tutar: {fiyat}")
indirimli_fiyat(50,100)