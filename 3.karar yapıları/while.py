sayi=1
while sayi<=10:
    print(sayi)
    sayi+=1
    #burada önce sayı değerini yazdırıp sonra 1 arttırıyor

sayi=0
while sayi<10:
    sayi+=1
    print(sayi)
#burada sayıyı 1 arttırıp sonra sayı değerini yazdırıyor bu yüzden 0 dan başlamalı ve <10 kullanılmalı 9 u bir arttırıp ekrana en son 10 vermesi için

while True:
    islem=input("yapmak istediğiniz işlemi seçiniz(+ - / *)")
    if islem=="+":
        print("toplama")
    elif islem == "-":
        print("çıkarma")
    elif islem == "/":
        print("bölme")
    elif islem == "*":
        print("çarpma")

#while True yapısı sonsuz döngüler için işe yarar bir yöntemdir kullanıcıdan veri girişin sürekli olduğu yerlerde kullanılır. örn: hesap makinesi