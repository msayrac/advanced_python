#%% global variable
# fonksiyonun blok ları icinde kullanılan degiskenler local variable

sayi1 = 10 # global variable
x=5

def func1():
    sayi=5 # local variable
    print(sayi)

# print(sayi) # gives error local variable

print(globals()) # program icindeki global degiskenleri goruntuleyebiliyoruz

print(globals()["x"]) # x global degiskenini degerini elde edebiliriz
print(globals()["sayi1"])

#%% recursive ve iterative functions
# iterative funct
def iterFunc():
    for i in range(1,11):
        print(i)
iterFunc()

# recursive func
print("***recursive func***")
def recFunc(sayi):
    if sayi ==0:
        return None
    print(sayi)
    recFunc(sayi-1)  
recFunc(10)

#%% recursive example

def iterFact(n):
    sonuc =None
    if type(n)== int and n>=0:
        sonuc =1
        for i in range(2,n+1):
            sonuc*=i        
    else:
        sonuc= "Lütfen dogal sayı giriniz!"
    return sonuc
    
print(iterFact(6))

print("*** iterative fact ***")
def  recFact(n):
    if type(n) == int and n>=0:
        if n == 0:
            return 1        
        return n * recFact(n-1)
    else:
        return "Lütfen dogal sayı giriniz!"

print(recFact(6))
        
#%% Lambda Anonymous Function (isimleri olmayan fonksiyonlar)

# lamda fonk ramde yer kaplamaz bir kere calısır. gecıcı olarak kullanılan fonk tanımlarız. bir sayının karesini tanımlama istersek

def kareAl(x):
    return x*x
print(type(kareAl))
print(kareAl(4))

lambdaKareAl = lambda x : x*x # x öyleki x*x karsılık geliyor : öyleki anlamına geliyor. assignment oldugu icin ram da kalıcı hale getirmis olduk.Normalde gecici olarak kullanırız
print(type(lambdaKareAl))
print(lambdaKareAl(3))

# toplama

lambdaTopla =lambda x,y : x+y # x ve y oyleki return olarak x+y doner
print(lambdaTopla(8,6))

#%% lambda example sayının küpünü alalım

kupAl = lambda sayi : sayi*sayi*sayi
kupAl2 = lambda s : s * s *s
print(kupAl(5))
print(kupAl2(5))

# string reverse yazdıran  lambda func

tersYaz = lambda str : str[::-1]
print(tersYaz("ali"))

#%% ozel fonk filter() map() reduce()

# filter()
#• pozitif sayıları bullalım
sayilar = [3,2,5,-7,14,4,-5,-6,-5,-3,11,110,-15]

for sayi in sayilar:
    if sayi>=0:
        print(sayi)
# bunu filter fonk ile daha kolay yapabiliriz

def pozitifMi(s):
    return s>0

pozitifMi(5) #True


pozitifSayilar = list(filter(pozitifMi,sayilar)) # pozitifMi fonk sayılar kısmına
print(pozitifSayilar)

negatifSayilar = list(filter(lambda s:s<0, sayilar))
print(negatifSayilar)

#%% tek cift sayı elde edelim

sayilar = [3,2,5,-7,14,4,-5,-6,-5,-3,11,110,-15]

ciftSayilar = list(filter(lambda s: s%2==0, sayilar))
print(ciftSayilar)

tekSayilar = list(filter(lambda x:x%2 != 0, sayilar))
print(tekSayilar)

def ciftMi(s):   
        return s%2 == 0

ciftSayilar1 = list(filter(ciftMi,sayilar))
print(ciftSayilar1)

#%% map() func --> dizi icindeki elemanların haritalanmasını saglayan fonk

# her bir elemanın karesini alalım

sayilar = [3,2,5,-7,14,4,-5,-6,-5,-3,11,110,-15]

def kareAl(s):
    return s**2

sayilarKaresi =list(map(kareAl,sayilar))
print(sayilarKaresi)
print("Lambda ve map kullanımı")
# list veya tuple formatında üretebiliriz
sayilarKaresi1 = tuple(map(lambda s: s**2, sayilar))
print(sayilarKaresi1)


#%% reduce() fonk indirgemek demek
# functools kutuphanesinden  reduce import etmemiz gerekiyor

from functools import reduce
sayilar = [3,4,6,-1,7]

def topla(s1,s2):
    return s1+s2
# reduce sayıları ikiserli alır yani s1 ve s2 olarak toplar
toplam = reduce(topla,sayilar)
print(toplam)

toplam2 = reduce(lambda x,y: x+y, sayilar)
print(toplam2)

# reduce ile carpma

sayilar = [2,1,6,5,4,8,-2,-4]

def carpma(x,y):
    return x * y

carpma = reduce(carpma,sayilar)
print(carpma)

carpma2 = reduce(lambda x,y : x*y, sayilar)
print(carpma2)

#%% en buyu ve en kuuck sayı bulan program reduce kullanalım
from functools import reduce
sayilar = [3,4,6,-1,7]
def enBuyukSayi(s1,s2):
    if s1>s2:
        return s1
    else:
        return s2
        
enBuyukSayi =reduce(enBuyukSayi,sayilar)
enbuyuSayi2 = reduce(lambda x,y: x if x>y else y,sayilar)     
print(max(sayilar),enBuyukSayi,enbuyuSayi2)

enKucukSayi = reduce(lambda a,b : a if a<b else b, sayilar)
print(enKucukSayi)

#%% zip fonksiyonu
# bilgilerin sıkıstırılmasını saglayan fonksiyonumuz
numaralar = [1,2,3,4,5]
isimler = ["Kaan","Arzu","Dilek","Kemal","Mehmet"]

ziplenmis = zip(numaralar,isimler)

bilgiler = list(ziplenmis)
print(bilgiler)

yaslar = [18,8,19,32,45]
bilgiler =list(zip(numaralar, isimler, yaslar))
print(bilgiler)

for bilgi in bilgiler:
    print(bilgi)

#%% map ve reduce example
from functools import reduce

katSayilar = [0.2,0.3,0.5]
notlar = [60,40,70]

donemSonuNotlar = []

for i in range(len(katSayilar)):
    donemSonuNotlar.append(katSayilar[i]*notlar[i])
print(donemSonuNotlar)

# map ile yapalım

donemSonuNotlar2 = list(map(lambda x,y:x*y,katSayilar,notlar))
print(donemSonuNotlar2)

donemSonuNotu = reduce(lambda x,y : x+y, donemSonuNotlar)
print(donemSonuNotu)

#%% enumerate, all, any

# enumerate fonk biizm verileir numaralandırmamız saglayan fonksiyondur

sayilar = (20,30,40,50,60)

for no, value in enumerate(sayilar,1): # 1 start degeri
    print("{}. sayi = {}".format(no,value))

set1 = {4,3,6,7,1}
print(list(enumerate(set1,1)))

rehber = {"Fatih": 10, "Selim": 20}

print(list(enumerate(rehber.items(),1)))
print(list(enumerate(rehber.keys(),1)))
print(list(enumerate(rehber.values(),1)))

#%% all() ve any() fonksiyonları
# all() --> buutn degerler True return degeri True olur
# any() --> en az bir deger True ise True donuyor

print(all([True,True,False])) # all --> hepsi True mu
print(any([False,False,True])) # any --> herhangi biri True mu

#%% bir fonk bir fonk return etmesi
def bilgiVer(func):
    print("Bilgi Veriliyor")
    return func


def kullaniciBilgisiVer(isim):
    return "Adı : " + isim

cikti = bilgiVer(kullaniciBilgisiVer("Ali"))
print(cikti)

#%% Decorators (Süslemeler)
# bir fonk ne kadar sure calısıtıgnı ogrenmek isityoruz

def funcInfo(func):
    def bilgiVer():
        print("Fonk Calısması Basladı!")
        func()    
        print("Fonk Calısması Bitti!")    
    return bilgiVer
@funcInfo # decorator soru sor calısınca bilgiler funcInfo icine gidiyor
def soruSor():
    print("Soru Sordum!")
@funcInfo
def cevapVer():
    print("Cevap Verdim!")

funcInfo(soruSor)()
funcInfo(cevapVer)()

# dekotaro kullanıca soruSor dogrudan calısır. yanı bır fonksıyon claısmadan once baska bır fonk calısmasını ıstersek burada soruSor() calısmadan once funcInfo fonksıyonu calısıyor gibi gibi ya da cevapVer()
soruSor()

cevapVer()

#%% decaratorler de Argumen iletimi

def funcInfo(func):
    def inner(*args,**kwargs):
        print("Konuşmaya başladı!")
        func(*args,**kwargs)
        print("Konuşmaya bitirdi!")        
    return inner
@funcInfo # soruSor() fonk calıstırılmadan once sen funcInfo calıstır
def soruSor(isim, yas, soru):
    print("soru soran kişinin bilgileri")
    print("Adı : {} Yaşı : {}".format(isim,yas))
    print(f"Sorusu : {soru}")

@funcInfo # cevapVer() fonk calıstırılmadan once sen funcInfo calıstır
def cevapVer(isim, yas, soru):
    print("Cevap Veren kişinin bilgileri")
    print("Adı : {} Yaşı : {}".format(isim,yas))
    print(f"Cevabı : {soru}")

funcInfo(soruSor)("Fatih",30,"Nasılsın")
funcInfo(cevapVer)("Kaan",25,"İyiyim")

#  @funcInfo decorator anahtar kelimesi ile dogrudan fonksiyonn kendi ismi ile cagırmamızı saglıyor
soruSor("Ali", 45, "Nerelisin")
cevapVer("Ahmet", 50, "İzmir")

#%% decorator ornekler

# kare hesaplayan ve fonk claısma suresini hesaplayan program

# zaman kutuphanesini import etmeliyiz
import time
# 1 Ocak 1970 den gunumuze kadar gecen sanıye hesaplar
print(time.time())

def calismaSuresi(func):
    def inner(*args,**kwargs):
        baslangic = time.time()
        func(*args,**kwargs)
        bitis = time.time()
        print("fonksiyonun calısma süresi : ", str(bitis-baslangic) + " sn dir")
    return inner

from math import sqrt
@calismaSuresi # decoder 
def kareKokAl(sayilar):
    sayilar = [sqrt(sayi) for sayi in sayilar]
    return sayilar
@calismaSuresi # decoder
def kareAl(sayilar):
    sayilar = [sayi**2 for sayi in sayilar]
    return sayilar


sayilar = list(range(0,20))

print(kareKokAl(sayilar))
print(kareAl(sayilar))

print(calismaSuresi(kareKokAl)(sayilar))
print(calismaSuresi(kareAl)(sayilar))

print(kareKokAl(sayilar))
print(kareAl(sayilar))
