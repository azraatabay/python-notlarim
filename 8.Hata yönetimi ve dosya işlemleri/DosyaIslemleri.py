#üretilen verileri kalıcı olarak depolamak ve ihtyiaç halinde çağırabilmek için dosya işlemlerine ihtiyaç duyarız

#dosya oluştururken ya da mevcut dosyaya giriş yaparken open() fnksiyonunu kullanılırız
#open("dosya yolu",mod)
#\n ,\t gibi özel karakterleri etkisiz hale getirmek için dosya yolunun başına r konulur
"""
dosya modları
w dosyayı yazma modunda açar
a dosyayı veri ekleme modunda açar
r dosyayı veri okuma modunda açar
"""
from fileinput import close

dosya=open("deneme.txt",mode="w")
dosya.write("merhaba ben azra") #write fonksiyonu ile açılan dosyaya veri yazdırdık
dosya.write("bugün hava çok güzel \n")
dosya.write("pyhton \n")
dosya.close()

dosya=open("deneme.txt",mode="a")
dosya.write("merhaba \n")
dosya.close() #dosyanın sürekli çalışmasını engellemek için vardır

dosya=open("deneme.txt","r")
print(dosya.read())  #dosyada yazılanları okur
dosya.close
print()

dosya=open("deneme.txt","r")
print(dosya.readline()) #dosyada yazılanları satır satır okur 1. satır
print(dosya.readline()) #2. satır
print(dosya.readline())  #3.satır
dosya.close
print()

dosya=open("deneme.txt","r")
print(dosya.readlines())  #dosyada yazılanları bir liste üzerinde okur
dosya.close
print()

dosya=open("deneme.txt","r")
satirlar=dosya.readlines()
for i in satirlar:
    print(i)

