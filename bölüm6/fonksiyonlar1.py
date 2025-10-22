#fonsiyonlar program içinde yer alan alt program parçalarıdır
#kodun modüler olmasını sağlar. komut isminden sonra () gelir. Parametreli ya da parametresiz olabilir
from bölüm1.veriturleri import mesaj


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
carpimlari, toplamlari=iki_islem(5,10)
print("Çarpımları:",carpimlari,"Toplamları:",toplamlari)

#varsayılan değerli parametreler
# parametrelere değer gönderilmemesi hata mesajı döndürür bunu engellemek için parametrelere varsayılan değer verilebilir
def mesaj_yaz(mesaj="cnm",adet=3):
    for i in range(adet):
        print(mesaj)
#burada adet sayısı kadar mesaj değerini döndüren bir fonksiyon vardır
mesaj_yaz("hello") #adet sayısı varsayılan olarak yazıldığından hata mesajı direkt 3 olarak aldı
mesaj_yaz("azrö",1) #burada adet sayısını fonksiyon içinde yazmasında rağmen biz bir değer verdiğimizde 1 olarak kabul etti
#aynı şekilde iki paramatreye de değer verebiliriz
mesaj_yaz() #parametreye bir değer girilmediği taktirde fonksiyon içindeki varsayılanları alır

#eğer mesaj varsayılanı olup adet olmazsa hata mesajı oluşturur!!!!!!!!
#varsayılan değerli bir parametreyi varsayılan değeri olmayan parametre takip edemez



