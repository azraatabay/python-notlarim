#input okunan veriler str cinsinden okunur bunun eğer sayısal işlem yapılacaksa tür dönüşümü gerekir

#int() komutu veriyi tam sayıya dönüştürmek için kullanılır
a="12"
b=int(a) #a str int e dönüştü
c=b+5
print(c)

a=int(input("Bir sayı giriniz:")) #girilen veri int cinsine dönüştürülüp işleme alınır
b=a+3
print(b)

a=3.4
b=int(a) #verilen ifadenin tam sayı kısmını aldırır
print(b)

#float komutu veriyi ondalıklı sayıya dönüştürmek için kullanılır
a=float(input("Bir sayı giriniz:"))
print(a)

#str komutu veriyi str olarak dönüştürür
a=85
print(str(a)+". cadde")

#chr() sayısal değer karakter karşılığına dönüştürür
a=chr(65)
print(a)

#ord() chr nin tam tersi
b=ord('A')
print(b)

#bool mantıksal karşlığı elde eder
print(bool(1))
print(bool(0))
print(bool(a))
print(bool(""))
#0 veya boş olan veriler haricinde true döndürür