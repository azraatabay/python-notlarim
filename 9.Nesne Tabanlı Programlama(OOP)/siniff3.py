class Calisan():
    def __init__(self):
        self.yetenekleri=["İngilizce biliyor"]
esra=Calisan()
eda=Calisan()
kerem=Calisan()

esra.yetenekleri.append("konuşkan")
eda.yetenekleri.append("zeki")
print(esra.yetenekleri)
print(eda.yetenekleri)
print(kerem.yetenekleri)
#böylece örnekler kullanarak birinin üzerine yaptığımız değişiklik diğer örnekleri etkilememiş oldu
