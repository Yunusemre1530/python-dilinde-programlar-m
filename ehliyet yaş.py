eğitim= input("eğitim durumunu giriniz: ")
yaş= int(input("yaşı giriniz: "))
if yaş>=18:
    if eğitim=="lise" or eğitim=="üniversite":
        print("ehliyet alabilirsiniz")
    else:
        print("öğrenim durumundan dolayı ehliyet alamazssınız")
else:
    print("ehliyet alamazsınız yaşınız küçüktür") 