#döngüyü sonlandırmak için kullanılırlar

#break
toplam=0
while True:
    sayi=int(input("sayı giriniz:"))
    if sayi<=0:
        break
    toplam+=sayi

kelime=("bilgisayar")
for i in range(kelime):
    if i=="s":
        break
    print(i)
