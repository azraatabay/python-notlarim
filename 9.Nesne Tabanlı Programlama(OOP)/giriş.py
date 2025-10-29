#OOP temelinde sınıf kavramı bulunur . Sınıflar nesne üretmemizi sağlayan veri tipleridir

sesli_harfler="aeıioöuü"
sayac=0
kelime=input("Bir kelime girin:")
def sesli(harf): #bu sesli harflerin içinde harf değişkenini gezdirir
    return harf in sesli_harfler
def arttır():  #bu fonksiyon kelimenin içinde sesli harf varsa sayacı arttırır
    global sayac  #buradaki global deyimi fonksiyon dışındaki değişkenin değerini değiştireceğimiz için belirtmemiz lazım global deyimi kullanılması çok tavsiye edilmez
    for harf in kelime:
        if sesli(harf):
            sayac+=1
    return sayac
mesaj= "{} kelimesinde {} sesli harf var"
print(mesaj.format(kelime,arttır()))
#-------------------------------------------------------------------------------------------------------------------------------
#bu şekilde de yazabiliriz sayac parametresi ekleyerek global kullamadan sayac üzerinde değişiklik yapabiliriz
sesli_harfler="aeıioöuü"
sayac=0
kelime=input("Bir kelime girin:")
def sesli(harf):
    return harf in sesli_harfler
def arttır(n):
    for harf in kelime:
        if sesli(harf):
            n+=1
    return n
mesaj= "{} kelimesinde {} sesli harf var"
print(mesaj.format(kelime,arttır(sayac)))
#--------------------------------------------------------------------------------------------------------------------------------------------



