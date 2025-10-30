class CalisanSinifi : #sınıf tanımlarken class deyimi ardından sınıf adı yazılır birden çok kelimeden oluşuyorsa ilk harfleri büyük yazılır
    pass

class Calisan():  #sınıf niteliklerine erişmek için sınıf adlarının paraantezsiz kullanmalıyız
    kabiliyetleri=[]
    unvani="işçi"
    maasi=30000
    memleketi=""
    dogum_tarihi=""
print(Calisan.kabiliyetleri)
print(Calisan.unvani)

ayse=Calisan()
fatma=Calisan()
ahmet=Calisan()  #sınıfı ahmet adlı değişkene atadık bu işleme örnekleme ya da örneklendirme denir
#bir fonksiyonu kullanışlı hale getirmeye "çağırma", bir sınıfı kullanışlı hale getirmeye "örnekleme" denir

class Asker():
    rutbesi="er"
    standart_techizat=["silah","süngü","el bombası"]
    gucu=60
    birligi=""

mehmet=Asker()  #burada Asker class ına referans oluşturduk bu isim üzerinden sınıftaki özelliklere erişebiliriz
#yani sınıfları bir isme atadığımızda örnekleme yapmış oluyoruz
#ahmet ve mehmet ilgili sınıların bütün özelliklerini taşıyan birer üyesidir. ingilizce karşılığı instance

class Siparis():
    firma=("")          #buradaki firma, miktar vs gibi değişkenler sınıf niteliğidir (class atribute)
    miktar=0
    siparis_tarihi=""
    teslim=tarihi=""
    stok_adedi=0

pamuk=Siparis()
kalem=Siparis()
elma=Siparis()
#bir class tan istediğimiz kadar örnek oluşturabiliriz. burada class özelliklerini sağlayan 3 tane üye meydana getirmiş olduk
kalem.siparis_tarihi
kalem.firma
