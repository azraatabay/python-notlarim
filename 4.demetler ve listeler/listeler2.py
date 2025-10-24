#liste parçalama
liste=[20,30,40,50,60,70,80]
print(liste[1:6:3]) #sırasıyla başlangıç indisi, bitiş indisi, artış
print(liste[6:1:-3])

#liste elemanlarını değiştirme
liste=[1,2,3,4,5,6,7]
liste[3]=40
print(liste)
liste[3:]=[10,30,50,70]
print(liste)

#liste birleştirme
liste1=[1,2,3,4]
liste2=[4,6,7,8]
liste3=liste1+liste2
print(liste3) #iki tane 4 olmasına rağmen teke indirmez iki listeyi olduğu gibi birleştirir
liste4=liste1+[5] #eğer bir eleman eklenecekse liste parantezi içinde eklenmelidir
print(liste4)

#liste çoğaltma
liste5=["a","b","c","d","e","f"]
a=liste5*2 #listedeki elemanları 2 katına çıkarmış olduk
print(a)

#listeye eleman ekleme
liste6=[10,"a",20,30,"b","c"]
liste6.append("d") #listenin en sonuna eklencek elemanlar için .append() kullanılır
print(liste6)

liste7=[1,2,3,4,5,6]
liste7.insert(3,3) #.insert(indis numarası,eklencek eleman)
print(liste7)
