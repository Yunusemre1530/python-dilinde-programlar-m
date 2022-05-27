renkler =  ["siyah","sarı","lacivert"]
sayılar = [-9,100,-99,56]
print(min(sayılar))
print(max(sayılar))
print(sum(sayılar))
for a in renkler:
    print(a)
print(list(enumerate(renkler,start=1)))
print(-99 in sayılar)
stringrenler=",".join(renkler)
print(stringrenler)
liste10=stringrenler.split(" ")
print(liste10)
print(renkler[0])