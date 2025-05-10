#%% Abstraction
from abc import ABC, abstractmethod
class Makine:
    @abstractmethod
    def calis(self):
        print("Makine calisti!")

class CamarisMakinesi(Makine):
    def calis(self):
        print("Camasir makinesi calisti!")
    
class BulasikMakinesi(Makine):
    
    def calis(self):
        print("Bulasik makinesi calisti!")


c1 = CamarisMakinesi()
b1 = BulasikMakinesi()

c1.calis()
b1.calis()


class Insan:
    def camasirYika(self,makine:CamarisMakinesi):
        if type(makine)==CamarisMakinesi:
            print("İnsans çamasırları makineye atttı")
            makine.calis()
        else:
            print("Bu makine de camasir yıkayamazsın")

i1 = Insan()
i1.camasirYika(c1)

#%% iterators --> yineleyici

sayilar = [1,2,3,4,5,6]
for sayi in sayilar:
    print(sayi)
#%%
# sayilari iterator yapalım iter()

sayilar1 = iter(sayilar)
print(sayilar1.__next__())
print(sayilar1.__next__())
print(sayilar1.__next__())
print(sayilar1.__next__())
print(sayilar1.__next__())
print(sayilar1.__next__())

#%% Generator --> üretecler yineleme durumu varıd iterator diyebiliriz
# yield --> ürün, verim
# yield --> ortaya urun uretmek ıcın kullanılan anahtar kelime

def sayiUret():
    yield 1
    yield True
    yield "Fatih Kaan Açıkgöz"

# fonk 3 tane deger uretti sonra bu degerleri listeye cektik
uretilmisDegerler = list(sayiUret())

for sayi in uretilmisDegerler:
    print(sayi)      
    
# ilk 100 sayi generator ile uretelim
def ilk100Sayi():
    i = 0 
    while i<=100:
        yield i
        i+=1
print(list(ilk100Sayi()))

#%%         Errors --> Hatalar
#Exception (olagandışılık, istisna)
#Handling (işleme, idare etme)

# 1-) Compile time errors (Derleme hataları)
#     syntactical errors (Dil bilgisi hataları)
#         : işaretini for veya if in sonuna koymamak gibi hatalar 

# 2-) Logical errors (mantıksal hatalar)
#     wrong output (yanlıs cıktı)
#         toplama fonksiyonuna 5 +6 = 10 cıkıyor 11 cıkmıyor vb mantıksal          hatalar 
# 3-)Rum time erros (calısma zamanında hatalar)
#     divide by zero bir sayıyı sıfıra boldugumuzdeki hataalr

# Statement -->
# Normal (warning - uyarı)
# Critical (Error - Hata)

#%% Value Error (deger hatası)
# zeroDivisionError (sıfıra bolme hatası)
# try deneme blogu 
try:
    sayi1 = int(input("Lütfen bir tam sayı giriniz : "))
    sayi2 = int(input("Lütfen bir tam sayı giriniz : "))
    print(f"sayi1/sayi2 = {round(sayi1/sayi2,4)}")
# tam sayı yerine kesirli sayı girerse
except ValueError: # except ile fırlatılan hatayı yakalıyoruz
    # handle bu blokta gerceklestirioyruz
    print("Lütfen Tam Sayı Giriniz")
except ZeroDivisionError:
    print("Real sıyı sıfıra bolunemez. Sıfır dısında bir sayı giriniz")

# farklı exceptionları google python exception yazarak bakabılırsınız

#%% Hata Görüntüleme ve finally Anahtar Kelimesi

sayi1 = 9
sayi2 = 0 # str(a) gibi hataları de Exception ile yakalarız

try:
    print(sayi1/sayi2)
# butun hataları Exception cagırarak yakalayabılırız
except Exception as e:
    print("Karsılasılan hata : ", e)
finally: # finally islemin sonlanmasını saglıyor
    print("İslemin sonlanmasını saglıyor")

#%% kendi hatalarımızı yakalama

def fact(n):
    if n < 0 or type(n) != int:
        raise ValueError("Sayı Dogal Sayı olmalıdır!")
    if n == 0:
        return 1 
    return n * fact(n-1)

def(5)










































































































































































































