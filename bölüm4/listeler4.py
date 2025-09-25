#listeyi küçükten büyüğe sıralama
from bölüm4.listeler2 import liste3

liste=[20,40,90,10,50,80]
liste.sort()
print(liste)

liste1=["elma","armut","kedi","kitap","kahve","ders"]
liste1.sort()
print(liste1)
#sort komutu küçükten büyüğe doğru sıralar. str ifadelerde alfabetik olarak sıralar

#listeyi ters çevirme
liste=[5,4,1,7,8,3]
liste.sort() #listeyi küçükten büyüğe sıraladı
liste.reverse() #listeyi tersine çevirdi
print(liste)

#liste içindeki bir elemanın kaç kere tekrar ettiğini bulma
liste=[1,1,7,7,75,4,7,3,4,7,9,45,7]
l=liste.count(7)
print(l)

#listenin en büyük ve en küçük elemanını bulma
liste=[1,1,7,7,75,4,7,3,4,7,9,45,7]
enbuyuk=max(liste)
enkucuk=min(liste)
print(enbuyuk)
print(enkucuk)
#str ifadelerde alfabetik olarak min max bulur

#liste elemanlarının toplamını bulma
liste=[1,1,7,7,75,4,7,3,4,7,9,45,7]
toplam=sum(liste)
print(toplam)

#liste üreteçleri
liste=[a for a in range(5)] #buradaki ilk a listeye ne koyucalak sorusunun cevabıdır ikinci a ise üzerinde gezilen değeri belirtir
print(liste)

liste=[a+1 for a in range(5)] #burada a+1 dediğimiz için listeye a değerinin 1 fazlasını yazdırdı
print(liste)

liste=[a for a in range(33) if a%2==0]
print(liste)

