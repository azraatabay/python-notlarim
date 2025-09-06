#sayısal türler
a=4
b=4.5
c=4+5j
print(type(a))
print(type(b))
print(type(c))

#karakter dizileri (string)
isim="Azra"
soyisim='Atabay'
print(isim, soyisim)
#stringler tek ya da çift tırnak içine yazılabilir hangisi ile başladıysan onunla . (""" """ bu da kullanılabilir)
mesaj="Azra 'Atabay'"
mesaj1='Azra"Atabay"'
print(mesaj,mesaj1)
#belirli formata sahip olanlar üç tırnak içinde yazılır
print("İstanbul","Ankara", sep="-") #sep ayraç parametresidir atanan ayracı aralara koyar
print(*"12345678", sep="-") #başına yıldız konularak daha pratik şekilde ayırma yapılabilir
print("Merhaba", end="!") #end parametresi ile en sona ne konulacağı belirlenebilir
#escape karakterleri
# "\" işaretinden sonra özel anlamları bulunan karakterlerdir
print("azra\natabay") #yeni satır
print("azra\tatabay") #tab kadar boşluk
print("azra/ratabay") #bulunduğu yerden satırbaşına kadar siler
#escape karakterlerini etkisiz hale getirmek için \ bir tane daha eklemek lazım veya string den önce satır başına r karakteri koymak lazım

#mantıksal veriler
m=2<3
print(m)



