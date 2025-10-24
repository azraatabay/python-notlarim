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

sozluk={"kedi":"cat","kalem":"pencil","elma":"apple","pen":"dolma kalem"}
for i in sozluk:
    print("Türkçe:" ,i, "İngilizce:",sozluk[i])
#sözlük içindekileri alt alta yazdırır

print(sozluk.items()) #sözlük içindeki key-value değerlerine aynı anda ulaşmayı sağlar

sozluk={"kedi":"cat","kalem":"pencil","elma":"apple","pen":"dolma kalem"}
for key, value in sozluk.items(): #burada key, value yazdığımız sözlükleri ikili çiftleri alıyor .items sayesinde ikili olarak ulaşılıyor zaten
    print("Anahtar:", key, "Değer:", value)

# .keys() anahtarlara ulaşır
# .values() değerlere ulaışır
for i in sozluk.keys():
    print(i)
for k in sozluk.values():
    print(k)

#eleman sayısını bulma len() ile yapılır aslında anahtar sayısı bulunur
print(len(sozluk))

#anahtar varlığını kontrol edilirken in ve not in kullanılır. Değer varlığı kontrol edilemez.
print("kedi" in sozluk)
print("pencil" in sozluk) #değerde olduğundan false verdi
print("pencil" not in sozluk)
print()


