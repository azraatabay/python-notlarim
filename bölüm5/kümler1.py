print(set()) #boş küme tanımlama
kume={1,2,3,4,5,6}
print(kume)

dersler=["Matematik","Türkçe","Biyoloji","Kimya"]
dersler_kumesi=set(dersler)
print(dersler_kumesi)
print(dersler) #listeleri kümelere dönüştürdük

#kümeye eleman eklemek için .add komutu kullanılır
dersler_kumesi.add("Fizik")
print(dersler_kumesi)
#kümeden eleman çıkarmak için .remove veya .discard komutları kullanılır
#kümede olmayan bir eleman silinmek istenirse remove hata verir discard hata vermez
dersler_kumesi.remove("Biyoloji")
print(dersler_kumesi)
dersler_kumesi.discard("Müzik")
print(dersler_kumesi)

kume1={5,10,15,20,25,30,35,40}
kume2={10,20,30,40}

#iki küme farkı almak için difference() komutu kullanılır
fark=kume2.difference(kume1) #küme2 de olup kume1  de olmayanları verdi
print(fark)
fark1=kume2-kume1 ##küme2 de olup kume1  de olmayanları verdi operatör kullandık
print(fark1)

#kesişim kümesini bulmak için .intersection komutu kullanılır
kesisim=kume2.intersection(kume1)
print(kesisim) #her iki kümede de olanları verdi
kesisim1=kume2&kume1
print(kesisim1) #her iki kümede de olanları verdi operatör kullanıldı

karakter="ÇçĞğŞşİıÖöÜü"
kelime=input("Lütfen bir keime giriniz:")
if set(karakter)&set(kelime): #set komutları ile kümeye dönüştülüp kesişim işlemi yaptık
    print("Girdiğiniz kelime Türkçe karakter barındırıyor.")
else:
    print("Girdiğiniz kelime Türkçe karakter barındırmıyor.")

#ayrık küme olup olmadığını kontrol etmek için .isdisjoint() komutu kullanılır
ayrik_mi=kume1.isdisjoint(kume2)
print(ayrik_mi)

#alt küme olup olmadığını kontrol etmek için .issubset() komutu kullanılır
altkume_mi=kume2.issubset(kume1)
print(altkume_mi)

#kapsayan küme olup olmadığını kontrol etmek için .issuperset() komutu kullanılır
kapsayankume_mi=kume1.issuperset(kume2)
print(kapsayankume_mi)

#birleşim kümesini elde etmek için .union() komutu kullanılır
birlesim=kume1.union(kume2)
print(birlesim)
birlesim1=kume1|kume2
print(birlesim1) #operatör kullanılarak birleşimleri alındı