#%%

print("Sesleniyorum")
print("Naber")
print("Nasılsın")
print("Seslenmeyi bitirdim")

# bizim gün icinde defalarca yaptıgımız seyleri tekrar tekrar yapmak istersek fonksiyonları kullanırız. daha az kod yazmıs oluruz. kendimizi tekrarlamaktan kurtuluruz

print("********Fonksiyon tanımlandı********")
def seslen():
    print("Sesleniyorum")
    print("Naber")
    print("Nasılsın")
    print("Seslenmeyi bitirdim")
    
seslen() # seslen blogu calısmıs oluyor


#%% parametresis fonksiyonlar
# dısarıdan veri dahil degil

def my_info():
    print("Adım : Ali")
    print("Soyad : Can")
    print("Üniversite : Sivas Cumhuriyet Ünv.")

my_info() # bu bilgileir istedigimiz zaman cagırabiliriz. 
my_info()
my_info()
my_info()

#%% fonk icinde fonk cagırabilir miyiz

def isim_soyle():
    print("Adım : Ali")
    print("Soyad : Can")
    
def my_info():
    isim_soyle()
    print("Üniversite : Sivas Cumhuriyet Ünv.")

my_info()
isim_soyle()

#%% parametreli fonksiyonlar
# dısarıdan veri alısı olur

def toplama(x,y):
    print("sayı1 : {} sayı2 : {} Toplam : {}".format(x,y,x+y))

toplama(3,5) # parametre degerini argumanları vermek gereklidir


def isimsoyle(isim, soyisim):
    print("{} {}".format(isim,soyisim))

isimsoyle("Ali","Can")

#%% return kavramı

# bir fonksioyn calıstıktan sonra ortaya bir urun cıkması kavramına denir

def bilgiver():
    print("Fatih Karan")

bilgiver()

#overring - gecersiz kılmak
def bilgiver(isim):
    print(isim)

bilgiver("Fatih Karan")

# return degeri fonksiyon calıstıkdan sonra ortaya cıkan urun degeri

urun = bilgiver("Ayca kapı")
print(urun) # none -- boyle bır urun yok diyor

# fonk icine return anahtar kelimesi kullanarak cıkarırız
print("***** return ****")
def bilgiver(isim):
    print(isim)
    return isim + " ile alakalı bilgi verildi."

urun = bilgiver("Ayça")
print(urun)

# sayi1 ve sayi2 parametresinin argumanını urun haline getirmis oluyoruz
def carpma(sayi1, sayi2):
    return sayi1 * sayi2

sonuc = carpma(3,5) #☻ bir degiskene atayabiliyoruz return ile
print(sonuc)
    
def carpma(sayi1, sayi2):
    print(sayi1 * sayi2)

sonuc = carpma(3,5) # return yoksa bir degiskene atama olmaz 
print(sonuc)    

#%% return ornek

def mutlakdegerCaprma(x,y):
    return abs(x * y)

print(mutlakdegerCaprma(-5, 6))

#♦ tuple olarak return birden fazla return degeri olustururuz otomatik olarak tuple olur ama [] ile list olarak da olusturabiliriz
def uckenKenarSoyle(k1,k2,k3):
    return ["Kenar1 : {}".format(k1), "Kenar2 : {}".format(k2), "Kenar3 : {}".format(k3)]
    
print(uckenKenarSoyle(3,4,5))

bilgi1, bilgi2, bilgi3 = uckenKenarSoyle(3,4,5)

print(bilgi1)
print(bilgi2)
print(bilgi3)

#%% daire alan ve cevre hesaplayan program
from math import pi
def daireAlanCevreHesapla(r):
    return [pi*r*r, 2*pi*r]
    
cevre, alan = daireAlanCevreHesapla(5)
print(cevre)
print(alan)

#%% PASS BY VALUE (Deger geçisi)
# PASS BY REFERENCE (Adres geçisi)

sayi1 = 10
sayi2 = sayi1 # deger esitlemesi yapıyorz

print(sayi1,sayi2)
sayi1 = 20
print(sayi1,sayi2)

liste1 = [10,20,30]
liste2 = liste1

print(liste1, liste2)

liste1[0]=75
print(liste1, liste2) # liste 2 degeride degisiyor. sebebi birden fazla degerleri tutan objelerin ozelligi  adress esitlemesi yapmıs oluruz

#%%
# pass by value deger gecisi oluyor
def guncelle(sayi):
    print("Sayi id", id(sayi))
    sayi=9
    print("Sayi id", id(sayi))
    print("Func Sayi", sayi)

sayimiz =20
print("Sayi id", id(sayimiz))
print("Sayi deger", sayimiz)

guncelle(sayimiz)

#%% pass by reference

def listeguncelle(liste):
    print("Func liste id : ", id(liste))
    liste[0]=1000
    print("Func liste id : ", id(liste)) # aynı adresteki eleman guncellendigi icin listemiz de etkileniyor
    
listemiz = [0,10,20,30]
print("Listemiz id : ", id(listemiz))
listeguncelle(listemiz)
print(listemiz)

#%% type of arguments

# positional arguments muhakkak verilmesi gereken degerler

def topla(x,y):
    return x+y
print(topla(5,6))

# posiitonal argument default deger atayabiliriz. vermek zorunda degiliz default argument
def topla(x,y=0):
    return x+y
print(topla(5))

# keyword bazı durumlarda argumentleri iletirken  x= deger y = deger keyword olarak deger gecisini saglayabiliriz
print(topla(x=5, y=9))

# variable length  birden fazla sayı alabiliriz. variable length uuznluga baglı degisken

def topla(*sayilar):
    print(sayilar)
    
print(topla(5,6,5,6,4))


def topla(s1, s2, *sayilar):
    print(s1,s2, sayilar)
    print(s1+s2+sum(sayilar))
print(topla(5,6,5,6,4))

#%% kwarg - key word arguments
# tek * ismi olmayan argumanları cift ** ise ismi olan argumanların tutulmasını saglar
 
def topla(s1,s2,*args,**kwargs):
    print(s1,s2,args)    
    print(kwargs)
    if(kwargs["islem"]=="+"):
        print("Yapılan islem toplama islemidir")
        print(s1+s2+sum(args))
    else:
        print("Bu fonksiyon toplama islemi dısında bir işlemi desteklememektedir")
    
topla(5,6,5,6,4,islem ="*")
    
#%% Positional Arguments (konumu belli argümanlar)

def hesapla(s1,s2, islem):
    if islem=="+":
        sonuc = s1+s2
    elif islem=="-":
        sonuc = s1-s2
    elif islem == "*":
        sonuc = s1 * s2
    elif islem == "/":
        try:
            sonuc = s1 / s2
        except:
            print(" 0 a bolme yapamazsınız")       
    elif islem == "%":
        sonuc = s1 % s2
    else:
        sonuc = "5 temel islem dıısnda hesaplama yapılmamaktadır"
    return sonuc
    
print(hesapla(5,2,"+"))   
print(hesapla(5,2,"-"))   
print(hesapla(5,2,"*"))   
print(hesapla(5,2,"/"))   
print(hesapla(5,2,"%")) 
print(hesapla(5,2,"//")) 

#%% keyword ve default arguments

def ogrenciBilgi(isim, numara,adres="",sube=""):
    print("Öğrencinin ismi : ",isim)
    print("Öğrencinin numara : ",numara)
    if adres != "":
        print("Öğrencinin adres :",adres)
    if sube != "":
        print("Öğrencinin sube :",sube)   

ogrenciBilgi("Fatih",197, "Besiktas","A")
ogrenciBilgi("Mehmet",198,sube="E")

# keyword argument parametre isimleriyle belirtiriz

#%% variable length argument * --> keyword u olmayan arguments (*args) ** ise keyword u olan arguments tutuyor (**kwargs)

def bilgileriGoster(*args,**kwargs):
    print(args)
    print(kwargs)
    
bilgileriGoster("Fatih","Kaan","Aysel", fatih=26, kaan = 29, aysel = 36) 

#%% variable length argument example
# sınırsız sayıda degerin karekokunu hesapla
from math import sqrt
def karekokHesapla(*args):
    for sayi in args:
        print(round(sqrt(sayi),4), sep="*", end="\n")

karekokHesapla(0,5,9,15,25,33)


