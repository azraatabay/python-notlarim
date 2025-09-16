#while a göre kullanım alanı daha geniştir.
#belirli bir sayıda tekrar etmesi istenen işler veya bir veri kümesi içindeki elemanlar üzerinde gezinmek için kullanılır

harfler="abcde"
for i in harfler:   #burada harfler içindeki her bir elemanı i değişkeni içinde saklanır
    print(i)

#range fonksiyonu
#belirli aralıkta sıralı sayılar üretmek için kullanılır
for sayi in range(10): #burada başlangıç 0 olarak kabul edilir
    print(sayi)

for sayi in range(7,12):
    print(sayi) #ilk sayı dahil son sayı haariç olarak alır

for sayi in range(3,11,4):  #ilk sayı başlangıç ikinci bitiş üçüncü artış miktarını belirler yine ilk dahil son hariç
    print(sayi)

for sayi in range(22,2,-2):
    print(sayi)  #geriye doğru sayar