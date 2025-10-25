"""
Fonksiyonlar yalnız aynı kod dosyası içerisinde yeniden çağırılabilirken modüller kodun daha sonra başka program dosyaları içerisinden
de çağırılabilir olmasını sağlar
"""

#modül ekleme
# daha önce yazılan modülleri kod dosyasına eklemek için import komutu kullanılır
"""
import math matematik işlemleri için
import calendar takvim işlemleri için
import time zaman işlemleri içinn
import os işletim sistemine ilişkin işler için"""

#modüllere takma isim verme

import math as islem        #random modülünün ismini rastgele olarak takma ad verdik
x=islem.ceil(4.3)
print(x)

#modüldeki belli bir kısım aktarılacaksa modül içindeki özellik adıyla eklenebilir sisteme yük getirmemek için kullanılır

from os import name
print(name)
from math import sin,radians #iki tane özelliği de bu şekilde ekleyebiliriz
print(sin(radians(30)))

#modül ön eki almadan modül özelliklerini kullanmak için import* kullanırız
from math import*
print(cos(radians(30))) #math ön eki kullanmadan yazdık

#bir modül altında yer alan özellikleri listelemek için dir() kullanılır
import math
icerik=dir(math)
print(icerik)