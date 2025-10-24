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
    if deneme not in rakamlar:
        pass
        print("Yanlış tahmin tekrar deneyiniz.")
    else:
        print("Tebrikler! Rakamı buldunuz.")
        break

rakamlar="2479"
while True:
    deneme=input("Bir rakam deneyiniz:")
    if deneme not in rakamlar:
        continue
        print("Yanlış tahmin tekrar deneyiniz.")
    else:
        print("Tebrikler! Rakamı buldunuz.")
        break

#ÖNEMLİ NOT! pass ile continue arasındaki fark continue eğer koşul sağlanmıyorsa döngüyü hemen sonlandırır sonraki bloğa geçmez
#pass ise hiçbir şey yapmadan devam et demektir koşul sağlanmıyosa bişey yapmaz sonraki adıma geçer
#Bu yüzden continue konulduğunda "Yanlış tahmin tekrar deneyiniz." çıktı olarak görünmez. Kodun bir sonraki adıma geçmesine izin vermeden başa döndürdüğü için.

#Ayrcıa pass komutu daha sonra kod eklenecek yerleri belirtmek için de kullanılabilir.



