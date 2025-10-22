#fonsiyonlar program içinde yer alan alt program parçalarıdır
#kodun modüler olmasını sağlar. komut isminden sonra () gelir. Parametreli ya da parametresiz olabilir
from bölüm5.kümler1 import birlesim


#fonksiyon tanımlama def fonksiyon_ismi(varsa paramerte(ler)
                      #fonskiyona ait kodlar
def message():
    print("merhaba")

def toplam(a,b):
    sonuc=a+b
    print(sonuc)
#fonksiyon çağırma
message()
toplam(10,30)

#fonksiyonun geriye değer döndürmesi
#ekrana yazma fonksiyon içinde olmazsa görüntülünemez. Eğer sonuç fonksiyon dışında kullanılmak için çağırılmasına geriye döndürme denir return ile yapılır
def topla(a,b):
    sonuc1=a+b
    return sonuc1
islem=topla(10,20)
print(islem)
#return başka bir fonksiyon için yazılabilmeyi sağlar

#return den sonraki ifadeler çalışmaz fonsiyon sonlanır
def carpim(a,b):
    sonuc2=a*b
    return sonuc2
    print("İşlem tamamlandı")

x=carpim(2,2)
print(x) #fonksiyonu çağırınca return den sonraki kısım yazılmadı

#birden çok değeri geri döndürme
def iki_islem(a,b):
    çarpim=a*b
    toplam1=a+b
    return çarpim,toplam1
degerr=iki_islem(5,10)
print(degerr)

