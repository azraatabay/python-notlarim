 #sözlükler üzerinde ekleme, çıkarma gibi düzenleme işlemleri yapılabilir
#key-value
#sozluk={key1:value1,key2:value2...} #bu şekilde tanımlanırlar hem key hem value değerleri belirlenebilir
sozluk={} #boş sözlük tanımlama

sozluk={"kedi":"cat","kalem":"pencil","elma":"apple","pen":"kalem"}
print(sozluk)
#sözlüklerde o elemana ulaşmak için key değeri kullanılmalıdır
a=sozluk["kedi"]
print(a)
b=sozluk.get("kalem")
print(b)
#.get komutu value değerini getirir eğer yoksa hata üretmez
c=sozluk.get("kitap")
print(c)

sozluk["kitap"]="book" #sözlüğe yeni key-value atandı
print(sozluk)

sozluk["pen"]="dolma kalem" #sözlük içindeki value değiştirildi
print(sozluk)

del sozluk["pen"] #sozluk içindeki key-value çifti silindi
print(sozluk)

sozluk.clear() #sözlük içinde tüm değerleri siler
print(sozluk)


