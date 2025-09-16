#if
yas=25
if yas>=18:
    print("Kişi yetişkindir")

#else
yas=30
if yas>=18:
    print("Kişi yetişkindir.")
else:
    print("Kişi yetişkin değildir.")

#elif
yas=int(input("Lütfen yaşınızı giriniz:"))
if yas>=65:
    print("Yaşlı")
elif 18<=yas<65:
    print("Genç")
else:
    print("Çocuk")