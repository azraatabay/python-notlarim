#pyhtondaki matematiksel hazır fonksiyonlar
#başına math. konulması gerekir bazı fonksiyonlar için
import math

from bölüm4.listeler4 import enbuyuk

#mutlak değer alma işlemi fabs() ya da abs() ile yapılır
a=math.fabs(-23)
print(a)
b=abs(-32)
print(b)
#abs() için import math gerekmez

#sayı yuvarlama işlemleri ceil() ,floor(), round()
#ceil() hep bir üst tam sayıya yuvarlar (tavan değer)
c=math.ceil(3.4435)
print(c)
d=math.ceil(2.0)
print(d)
#floor() hep alt tam sayıya yuvarlar
x=math.floor(4.623423)
print(x)
y=math.floor(4.0)
print(y)
#round() ondalıklı kısım 0.5 ten küçükse alta büyükse üste yuvarlar 0.5 ise alta yuvarlar. math. gerektirmez
m=round(10.5)
print(m)
n=round(32.4324)
print(n)
k=round(23.75354)
print(k)

#üs alma işlemi pow()
a=math.pow(3,2)
print(a)
print(3**2)

#karekök alma işlemi sqrt()
c=math.sqrt(43)
print(c)

#logaritma işlemi log()
x=math.log(8,2)
print(x)

#trigonometrik işlemler
#açı ölçüsü birimi radyandır
#dereceyi radyana çevirmek için radians() kullanılır
a=math.radians(270)
print(a)
sinus=math.sin(a)
kosinus=math.cos(a)
tanjant=math.tan(a)

#max min fonksiyonları math den bağımsız
sayilar=[32,4,24,13,53,5,23,12,54]
enbuyuk=max(sayilar)
enkucuk=min(sayilar)
print("Dizideki en büyük eleman:",enbuyuk,"Dizideki en küçük eleman:",enkucuk)

#toplam fonksiyonu sum()
toplam=sum(sayilar)
print(toplam)

#divmod() bir sayının başka bir sayıya bölümünden elde edilen bölüm ve kalanı aynı anda veririr
print(divmod(50,3))

#ikilik tabana dönüştürme bin() çıktıda 0b ön takısı binary olduğunu belirtir
sonuc=bin(5)
print(sonuc)
#int() ile
print(int(sonuc,2))