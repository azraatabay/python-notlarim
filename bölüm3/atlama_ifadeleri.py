#döngüyü sonlandırmak için kullanılırlar

#break
toplam=0
while True:
    sayi=int(input("sayı giriniz:"))
    if sayi<=0:
        break
    toplam+=sayi
print("toplam:",toplam)


kelime="bilgisayar"
for i in kelime:
    if i=="s":
        break
    print(i)

#continue
#döngüyü tamamen sonlandırmaz sadece mevcut adımı sonlandırır
for i in range(10): #0 ile 9 arasındaki sayıları i değerine atayarak döner
    if not i%2==0:  #eğer i değerinin iki ile bölümünden kalan 0 değil ise...
        continue   # o sayıyı ekrana yazdırmaz geç der o adımda döngü yazdırılmadan tekrar başa döner
    print(i)

cumle="merhaba ben Azra bilgisayar mühendiliği ikinci sınıf öğrencisiyim"
harf="aeuüoöıi"
for i in cumle: #i cümle içinde dönüyor
    if i in harf: #eğer i harf içindekinde bulunuyorsa
        continue #geç
    print(i)

#pass
#hiçbir şey yapmadan devam et anlamına gelir
rakamlar="2479"
while True:
    deneme=input("Bir rakam deneyiniz:")
    if rakamlar not in deneme:
        pass




