
import sinif1
print(dir(sinif1.Siparis)) #sinif1 dosyasında birden fazla class olduğundan dosya içindeki hangi class olduğunu belirtmemiz lazım

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
