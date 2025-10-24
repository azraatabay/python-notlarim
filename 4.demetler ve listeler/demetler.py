#listeler ile çok benzerdir ancak üzerinde ekleme,silme gibi düzenleme yapılmaz. Salt okunur listelerdir
from bölüm4.listeler4 import toplam

demet=tuple() #boş demet
demet=() #boş demet

demet=tuple([1,2,"kalem","silgi",2.3,4.2])
demet=(1,2,"kalem","silgi",2.3,4.2)
demet_indis=demet[1] #indis numarası ile elemana ulaşılması
print(demet_indis)
#burada indislerin değerlerine başka değer atanmak istenirse hata mesajı alınır çünkü tuple lar değiştirilemez
uzunluk=len(demet) #tuple ın uzunluğunu buldurur
print(uzunluk)
print(demet) #tuple ı ekrana yazdırır
for i in demet: #ekrana tek tek yazdırır
    print(i)

#demetlerde de parçalama işlemi listeler ile aynıdır
#demet(başlangıç:bitiş:artış) şeklindedir

#in, not in ve index() aynıdır

tekrar=demet.count(2) #kaç kere tekrar ettiğini bulur
print(tekrar)

#min max aynıdır

demet=(1,2,3,4,5)
toplam=sum(demet) #eleman toplamını buldurur listeler ile aynıdır
print(toplam)