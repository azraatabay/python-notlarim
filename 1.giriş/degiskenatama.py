#atama işlemleri her zaman sağdan sola doğru olur.
#öncelikle sağ taraftakki işlem gerçekleştirilip sonrasında değere atanır.

a=5
a=+10 #a=a+10 ile aynı anlamdadır
print(a)

#zincirleme atama
a=b=c=d=100
print(a)
print(b)
#bu durumda 100 değeri önce d ye. d c ye . c b ye. b a ya atanır.

#eş zamanlı atama
x,y,z=1,2,3
print(x,y,z) #sırasıyla atandı

a=40
b=50
print(a,b)
a,b=b,a
print(a,b) #değişkenlerin yerlerini değiştirmiş olduk

