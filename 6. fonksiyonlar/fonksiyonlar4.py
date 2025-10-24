#string fonksiyonlar

#replace
str="merhaba ben Azra bilgisayar mühendisliği öğrencisiyim"
yeni=str.replace("m","M")
print(yeni)
print()
yeni1=str.replace("merhaba","MERHABA")
print(yeni1)
print()
yeni2=str.replace("e","")
print(yeni2)
print()
yeni2=str.replace("m","M",1) #en sona count değeri eklenerek hangi değer silinmek istiyosa onu işretleriz
print(yeni2)
print()

#upper fonksiyonu tüm karakterleri büyük hale getirmek için kullanılır
buyuk=str.upper()
print(buyuk)
print()

#lower fonksiyonu tüm karakterleri küçük hale getirmek için kullanılır
kucuk=str.lower()
print(kucuk)
print()

#capitalize fonksiyonu strin verinin yalnızca ilk harfini büyük diğer harfleri küçük yapar
yeni3=str.capitalize()
print(yeni3)
print()

#title fonksiyonu string içindeki her kelimenin ilk harfini büyütmek için kullanılır
yeni4=str.title()
print(yeni4)
print()
#swapcase büyük harfleri küçük, küçük harfleri büyük yapar
yeni5=str.swapcase()
print(yeni5)

#strip ,lstrip,rstrip sting ifadede yer alan boşluk ve özel karakterler gibi gereksiz karakterleri temizlemek için kullanılır
str1="  merhaba  "
print(str1.strip())
print(str1.lstrip())
print(str1.rstrip())
str2="ayva" #kendi belirlediğimiz başta ya da sonra bulunan karakterileri de silebiliriz
print(str2.strip("a"))
print(str2.lstrip("a"))
print(str2.rstrip("a"))

#startswith ve endswith fonksiyonları bir string ifadenin belirtile karakter ya da kelime grubuyla başlayıp başlamadığını kontrol eder
str3="merhaba"
print(str3.endswith("ba"))
print(str3.startswith("her"))

#format fonkisyonu
a=3
b=4
sonuc="{}+{}={}".format(a,b,a+b)
print(sonuc)  #ekrana direkt sonuç olarak değil str ifade ile yazılmasını sağlar
