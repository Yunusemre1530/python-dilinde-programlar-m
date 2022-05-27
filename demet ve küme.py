küme= {"sarı","siyah","yeşil","lacivert"}
for a in küme:
    print(a)
küme.add("maraş")
print(küme)
küme.remove("lacivert")#kümede olmayan elemanda hata verir
for a in küme:
    print(a)
küme.discard("malatya")#kümede olmayanda hata vermez
print(küme)
küme2= {"sarı","siyah","yeşil","bej","gri"}
print(küme.intersection(küme2))
print(küme.union(küme2))
print(küme.difference(küme2))