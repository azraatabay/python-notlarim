#listeden eleman silme ve çıkarma
liste=[10,10,20,20,20,30,40]
liste.remove(20) #birden fazla aynı elemandan varsa sadece ilk gördüğünü siler
print(liste)

liste=[1,2,3,4,5,6,7]
del liste[5] #5. indisteki değeri siler
print(liste) #eğer del liste olarak yazılsaydı listeyi tamamen silerdi listeye ulaşılamazdı

liste=[50,60,70,80]
a=liste.pop() #listedeki son elemanı a değişkenine aktarır ve listeden siler
print(a)
print(liste)
b=liste.pop(2) #listedeki 2. indisli elemanı b değişkenine artarır ve listeden siler
print(b)
print(liste)

#listedeki elemanın varlığını kontrol etme
liste1=["a","b",1,2,4,5,"h",5]
kontrol= 1 in liste1
print(kontrol)
kontrol2= 2 not in liste1
print(kontrol2)
indis=liste1.index(5) #5 elemanının listedeki indisini gösterir
print(indis)
indis2=liste1.index(5,6) #ilk değer aranacak elemanı ikinci değer hangi indisten sonra aramaya başlayacağını belirtir
print(indis2)

liste1=[10,20,30]
liste2=liste1 #liste1 liste2 ile kopyalandı
print(liste2)
print(id(liste1))
print(id(liste2))
#bellekte aynı id olarak tutulurlar dolayısıyla birinde olan değişilklik diğerini de etkiler

liste3=[1,2,3]
liste4=liste3[:] #bu durumla liste3 içindekiler liste4 e kopyalanmış olur bellekte tutulma adresleri farklıdır
print(liste4)    #aralık belirterek bir kısmı da kopyalanbilir
print(id(liste3))
print(id(liste4))
#ayrı bellek yerlerinde tutulur



