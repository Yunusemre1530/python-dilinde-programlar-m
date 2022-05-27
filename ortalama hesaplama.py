vize= int(input("vizeyi giriniz: "))
final=int(input("final notunuzu giriniz: "))
ortalama=vize*(4/10)+final*(6/10)
if final<55:
    print(f"{ortalama} ama finalden kaldınız")
else:
    if ortalama>=85 and ortalama<=100:
        print(f"ortalamız {ortalama} notunuz A")
    if ortalama>=70 and ortalama<85:
        print(f"ortalamız {ortalama} notunuz B")
    if ortalama>=55 and ortalama<70:
        print(f"ortalamız {ortalama} notunuz C")
    if ortalama>=0 and ortalama<55:
        print(f"ortalamız {ortalama} notunuz D")
        print("kaldınız")
