#listeler aynı ya da farklı türden birçok elemanı bir arada tutar. Ekleme, silme, güncelleme işlemleri yapmaya olanak tanır.
#list() ya da [] olarak kullanılabilir

liste=list() #boş liste
liste=[] #boş liste

#liste içindeki eleman numaraları(indis) 0 dan başlar

liste=[23,24,76,"bilgisayar",48,1,"kalem","kitap"]
a=liste[1] #listedeki elemanı başından bulmak için 0 dan başlar
print(a)
b=liste[-5] #sondan eleman bulmak için indiş numaraları -1 den başlar -1 -2 -3 -4...
print(b)

uzunluk=len(liste)  #len komutu ile aynı zamanda str uzunluğu da bulunabilir
print(uzunluk)

c=liste[len(liste)-1] #en sondaki elemanı bulmak için liste uzunluğundan 1 çıkardık çünkü indis no 0 dan başlar
print(c)

for i in liste:
    print(i)

liste2=[40,30,70]
for i in range(0,len(liste2)):
    liste2[i]*=2 #listedeki her elemanı iki ile çarp tekrar kendine ata demek
print(liste2)

liste3=[10,20,30,"a","b","c","d",70,80]
for i in range(0,len(liste3),3):
    print(liste3[i])