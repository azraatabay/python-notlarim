import sinif1
print(dir(sinif1)) #doysa içinde tek class var zaten hangi class olduğunu belirtmeye gerek yok
print()


from sinif1 import Siparis #bunu kullanmak kodun okunabilirliğini artırır çünkü nereden geldiği belli
pamuk= sinif1.Siparis
print(dir(pamuk))
pamuk.miktar=5
print(pamuk.miktar)

from sinif1 import Calisan
ahmet=Calisan()
ayse=Calisan
fatma=Calisan
print(ahmet.kabiliyetleri)
print(ahmet.unvani)
ahmet.kabiliyetleri.append("prezentabl")
print(ahmet.kabiliyetleri)
print(ayse.kabiliyetleri) #burada görüldüğü gibi aynı class ta tanımlanan diğer örnekleri de etkiler (class nitelikleri )
# bunun olmasını istemiyorsak örnek niteliklerindden yararlanırız

#__init__ fonksiyonu ve self
class Calisan():
    personel=["a"]  #init self fonk içine yazmadık başına self eklememize gerek yok
    def __init__(self):
        self.kabiliyetleri=[]    #bir kodu init self içine yazıyosak oluşturduğumuz niteliğin başına self ekleyip örnek haline getirmeliyiz
        print(self.kabiliyetleri)
Calisan()
ahmet=Calisan() #çıktı için örnekleme çıkarmamız gerekiyor self kelimesi ahmeti temsil ediyor
print(ahmet.kabiliyetleri)
print(ahmet.personel)

class Calisan():
    kabiliyetleri=["sınıf niteliği"]
    def __init__(self):
        self.kabiliyetleri=["örnek niteliği"]
mehmet=Calisan()
ayse=Calisan()
fatma=Calisan()
print(mehmet.kabiliyetleri)  #bu durumada önce self içinde aradığından örnek niteliği çıktısını veririr çünkü örnek adı kullandık 'mehmet'
print(Calisan.kabiliyetleri) #bu durumda sınıf niteliği olanı verir çünkü sınıf adını kullandık 'Calisan'

"""
özetle örnek niteliği tanımlıyorsakbu niteliğin başına self getirmemiz lazım (self.kabiliyetleri) self kelimesini de __init__fonkisyonunun
ilk paramtersi olarak yerleştirmeliyiz. Örnekler sadece fonksiyonlar içinde tanımlanabilir bu kelime self olmak zorunda değil kendimiz
herhangi bir şey diyebiliriz mesela...
"""
class Supermarket():
    def __init__(canim):
        canim.reyonlar=["elma, artmut"]
market1=Supermarket()
print(market1.reyonlar)
#yani sınıf içindeki fonksiyonun ilk parametresi fonksiyon içindeki örnekleri temsil eden kelimedir
#yine de örnek niteliklerini temsil etmek için her zaman self kullan


