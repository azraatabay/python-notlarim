#fonksiyon çağırımlarında isimleri kullanılarak ya da kullanılmadan değer aktarımı yapılabilir
from bölüm6.fonksiyonlar1 import carpim


def sekil(karakter,sutun,satir):
    for i in range(satir):
        print(karakter*sutun)
sekil("*",2,3) #îsimlerini belirtmedik fonksiyondaki sırada yazmamız gerekir
print()
sekil(satir=3,sutun=2,karakter="*") #yine aynı sonuç çıkar isiimlerini belirttik
print()
sekil("*",satir=3,sutun=2) #hem isim belirtip hem belirtmiyceksek isimsizleri fonksiyonlardaki sırasında vermeliyiz
#ilk parametreden itibaren isimli olarak verildiyse öyle devam etmelidir isimsiz yazılırsa hata verir
print(*"1234") #baştaki yıldız sayesinde aralara birer boşluk koyar

#değişken sayıda parametre alabilen fonksiyonlar
def topla(*sayilar):    #buradaki baştaki * işaretinin amacı farklı sayılarda gelen paramterleri bir koleksiyon haline getirmek
    sonuc=0
    for i in sayilar:
        sonuc=sonuc+i
    return sonuc
toplam=topla(1,4,3,2,4)
print(toplam)
print()

#rekürsif fonksiyonlar kendi içerisinde kendini tekrar eder
def faktoriyel(sayi):
    carpim=1
    for i in range(sayi,1,-1):
        carpim=carpim*i
    return carpim
cevap=faktoriyel(3)
print(cevap)
print()

def faktöriyel2(sayi):
    if sayi==1:
        return 1
    return sayi*faktöriyel2(sayi-1)
cevap=faktöriyel2(3)
print(cevap)
print()

def fibonacci(sira_no):
    if sira_no==1 or sira_no==2:
        return 1
    return fibonacci(sira_no-1)+fibonacci(sira_no-2)
cevap2=fibonacci(10)
print(cevap2)
