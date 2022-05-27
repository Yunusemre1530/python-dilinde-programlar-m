bilgiler= {"adı": "yunus emre", "soyadı": "cinbolat", "yaş": "20","bölümmü": "yazilim"}
print(bilgiler)
bilgiler["yaş"]="21"
print(bilgiler)
#bilgiler.update({"adı": "fahreddin": "yaşı": "19","bölümü": "diş protez"})
#print(bilgiler)
bilgiler["id"]=12345
print(bilgiler)
del bilgiler["id"]
print(bilgiler)
print(bilgiler.keys())
print(bilgiler.values())
for yaz,v in bilgiler.items():
    print(yaz,v)
print(bilgiler.get("ıd","yok bu gerizakalı"))