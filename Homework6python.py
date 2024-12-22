"""
** BankaHesabi isminde bir sınıf tanımlayınız.
** Üretilen her bir nesne "hesapSahibi" isminde bir özelliğe sahip olmalıdır. BankaHesabi("Ad Soyad")
** Üretilen her bir nesne "bakiye" isminde bir özelliğe sahip olup başlangıçta 0.0 değerinde olmalıdır.
** Üretilen her bir nesne için "paraYatir" metodu oluşturun ve dışarıdan yatırılacak miktar bilgisini alıp bakiye
   üzerine ekleyin ve bakiye miktarını geriye döndürün.
** Üretilen her bir nesne için "paraCek" metodu oluşturun ve dışarıdan çekilecek miktar bilgisini alıp bakiye
   değerinden çıkarıp geriye döndürün.

    hesap = BankaHesabi("Ad Soyad")
    hesap.hesapSahibi => Ad Soyad
    hesap.bakiye => 0.0
    hesap.paraYatir(1000) => 1000.0
    hesap.paraCek(500) => 500.0
"""
class BankaHesabi:
    def __init__(self,hesapSahibi):
        self.hesapSahibi=hesapSahibi
        self.bakiye=0.0
    def paraYatir(self,para):
        self.bakiye+=para
        return self.bakiye
    def paraCek(self,para):
        self.bakiye-=para
        return self.bakiye
    
h1=BankaHesabi("Oray Bey")
h2=BankaHesabi("Koray Bey")
h3=BankaHesabi("Halime Teyze")
print(h1.hesapSahibi)
print(h2.bakiye)
print(h3.paraYatir(1000))
print(h3.bakiye)
print(h1.paraCek(500))
print(h1.bakiye)
        