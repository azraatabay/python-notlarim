#tarih ve zaman işlemleri için calender ve time modülleri kullanılır
#time() fonksiyonu zamanı tick formunda verir
#tick bir saniyeyi oluşturan en küçük zaman parçalalarıdır ondalıklı sayıdır
import time
from email.utils import localtime

print(time.time()) #güncel zaman bilgisini verir

#yerel zaman görüntüleme için localtime() kullanılır
print(time.localtime())
#bu liste içindeki bir bilgiye ulaşmak için sıra numaralarını kullanmalıyız
guncel_zaman=time.localtime()
print(guncel_zaman[8]) #8 numarada yaz saati uyg. olup olmadığı

#zamanı biçimlendirerek görüntülemek için asctime() komutu kullanılır
print(time.asctime())
#zamanı istenen foröatta görüntülemek için strftime() komutu kullanılır
print(time.strftime("%d %m %y %H:%M:%S "))

"""
%d (rakam olarak gün
"""

#takvim işlemleri için calender modülü kullanılır
import calendar
print(calendar.calendar(2025)) #tüm 2025 yılının takvimini görüntüler
print()
print(calendar.month(2025,10)) #o yıla ait ayı görüntüler

# herhangi bir yılın artık yıl olup olmadığını kontrol etmek için .isleap kullanılır(her sene olan 6 saat fazlalıktan kaynaklanan)
print(calendar.isleap(2025))