#aitlik operatörleri
#herhangi bir elemanın o koleksiyonda olup olmadığını kontrol eder
a="merhaba benim adım Azra burada pyhton notlarımı paylaşıyorum."
print("merhaba" in a) #merhaba stringi a nın içinde bulunuyor mu
print("okul" in a)
print("okul" not in a) #okul stringi a nın içinde bulunmuyor mu

#kimlik operatörleri
# iki nesnenin bellek adreslerini karşılaştırır. Değişkenler aynı bölgede ise is değilse is not
a=20
b=30
c="merhaba"
d=20
print(a is b)
print(a is not c)
print(a is d)
