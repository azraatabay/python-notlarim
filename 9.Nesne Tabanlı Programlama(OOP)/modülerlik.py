sesli_harfler="aeıioöuüAEIİUÜOÜ"
sayac=0

def kelime_sor():
    return input("Bir kelime giriniz:")

def sesli(harf):
    return harf in sesli_harfler

def arttır(sayac,kelime):
    for harf in kelime:
        if sesli(harf):
            sayac+=1
    return sayac

def ekrana_yazdir(kelime):
    mesaj = "{} kelimesinde {} sesli harf var"
    print(mesaj.format(kelime,arttır(sayac,kelime)))

def calistir():
    kelime=kelime_sor()
    ekrana_yazdir(kelime)

if __name__== "__main__":
    calistir()
#kodları küçük parçalara bölmek onları daha anlaşılabilir ve yönetilebilir yapar: modüler bir hale gelir
#bölyece kodların okunaklığı artar ve bakımı kolaylaşır



