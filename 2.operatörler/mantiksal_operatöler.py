#ve, veya , değil işlemleridir

yas=18
cinsiyet="kadın"
print(yas>=18 and cinsiyet=="kadın")

yas=15
cinsiyet="kadın"
print(yas>=18 and cinsiyet=="kadın")
#ve operatörü sadece iki durumun da doğru olduğu durumlarda true sonucunu verir

sicaklik=25
saat=14
print(sicaklik>20 or saat<14)

sicaklik=20
saat=15
print(sicaklik>20 or saat<14)
#veya operatörü iki durumdan herhangi birinin veya her ikisinin de sağlandığı durumlarda doğru sonucunu verir

kilo=60
print(not(kilo>50))
# not işlemin değilini alıyor normalde kilo değeri 50 den büyük ama başında not olduğundan false sonucu döndürür
