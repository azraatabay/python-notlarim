#hata yönetimi ortaya çıkan hataları ele alıp yönetir ve hata durumunda programın çalışmasını durdurmadan devamlılığını sağlar
#kod yazarken ImportError, NameError,OverflowError, Syntaxerror gibi gibi çeşitli hataları ortaya çıkabilmektedir
from logging.config import listen

#hata ayıklama için try / except ifadeleri kullanılır
#hata oluşturma ihtimali olan kodlar try bloğu içine yazılır hata oluşursa try çalışmayı durdurur ve except bloğu çalışır. Hata olmazsa except çalışmaz
try:
    a=int(input("ilk sayıyı giriniz:"))
    b= int(input("ikinci sayıyı giriniz:"))
    sonuc=a/b
    print(sonuc)
except:
    print("Tam sayı dışında bir değer girdiniz. Lütfen tekrar deneyin.")

#bu hata kodlarının neden ortaya çıktığını farklı açıklamalarla belirtmek daha açıklayıcı olur
try:
    a = int(input("ilk sayıyı giriniz:"))
    b = int(input("ikinci sayıyı giriniz:"))
    sonuc = a / b
    print(sonuc)
except ValueError:
    print("Tam sayı dışında bir değer girdiniz. Lütfen bir tekrar deneyin.")
except ZeroDivisionError:
    print("Bölüm sıfır olamaz. Lütfen tekrar deneyin.")
except:
    print(
        "Beklenmeyen bir hata oluştu.")  # yukarıdaki hatalar dışında bir hata olursa bu kod bloğu çalışır. en sona yazılmalıdır
finally:
    print("İşlem sonlandı")
#finally bloğunda hata olsun olmasın kesinlikle çalışmasını istediğimiz kodlar varsa buraya yazılır

#normal şartlarda hata oluşturmayan durumlar kendi programımız hata kabul edilebilir. Hata mesajları üretmek için raise terimi kullanılır

a=int(input("Bir tam sayı değeri giriniz:"))
if a>100:
    raise Exception("Girilen sayı 100 den büyük olamaz")

#iddialar- assertion
print("Kullanıcı bilgilerinizi giriniz.")
kullanici_adi=input("Kullanıcı adı:")
assert kullanici_adi=="azra"
sifre=input("Şifre:")
assert sifre==("1234")
print("Hoşgeldiniz.")
#assert değerleri girilmediği sürece hata döndürür

sicaklik=int(input("Hava kaç derece?"))
assert sicaklik>=25 ,"Hava soğuk"
print("Bugün hava çok güzel")









