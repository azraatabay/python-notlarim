
#sözlüklerin eşitliklerini kontol ederken == ve != kullanılır. Anahtara değer çifleri eşit mi kontrol edilir

market1= {"elma":20, "armut":40, "portakal":10}
market2={"kek":60, "cips":50, "kraker":40}
esitlik1= market1==market2
esitlik2= market1!=market2
print(esitlik1)
print(esitlik2)
print()
kırtasiye1= {"kalem":10, "defter":20}
kırtasiye2= {"defter":20, "kalem":10}
esitlik3= kırtasiye1==kırtasiye2
esitlik4= kırtasiye1!=kırtasiye2
print(esitlik3)
print(esitlik4)

#sözlük güncelleme için update() komutu kullanılır
coffee_price={"latte":100, "americano": 75, "filtre": 80, "espresso": 40 }
print(coffee_price)
coffee_new_price={"latte":200, "americano": 150, "filtre": 160 , "espresso": 80,"çay":50 , "bitki çayı":80}
coffee_price.update(coffee_new_price)
print(coffee_price.items()) #burada önceki fiyatlar güncellendi ve olmayanlar eklendi

#sözlük elemanlarının hepsini silmek için .clear kullanılır. sözlük boş hale gelir
print(coffee_price.clear())

#sözlüğü bellekten silme .del ile yapılır
#coffee_price.del bundan sonra silineceği için yazdırılmak istenirse hata alınır
print(coffee_price)

#sözlük kopyalama bellekte aynı yerde tutma
manav={"kivi":50,"ananas":80,"avakado": 40}
supermarket=manav
print(id(manav))
print(id(supermarket))
manav["kivi"]=45
#id ler aynı olur çünkü birbirine kopyalanınca bellekte aynı yerde tutulurlar.Birinin üzerinde yapılan değişiklik diğerini de etkiler
print(supermarket)
print()

#sözlük kopyalama farklı belleklerde tutulması
sarkuteri={"et":700,"tavuk":300,"yumurta":10}
market=sarkuteri.copy()
print(market)
sarkuteri["pastırma"]=1000
print(market)
print(sarkuteri)
#burada yapılan değişiklik sadece bir yeri etkiledi çünkü bellekte farklı yerlerde tutuluyor birbirlerini etkilemiyorlar
