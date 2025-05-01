#%% Data Types

# NoneType tipi olmayan obje ya da null olarak

sehir =None #tanımlanmamıs
print(type(sehir))
sehir = "İstanbul"
print(type(sehir))

#%% NUmeric types

# int float
x=10 # int
y=5.4 # float
z = int(y) # int
k=float(x) # float
print(x)
print(k)

#%% bool data type True or False

key1=True
key2=False
k1 = 3<5 # True

k2 = bool(True)
k3 = bool(False)

a1= bool(10)
print(a1)

a2 = int(True) # 1 elektrik var
a3 = int(False) # 0 elektrik yok

print(a2) 
print(a3)

print(float(a2)) 
print(float(a3))

#%% Complex numbers  j ile gösterilir

k1 = 2+3j
k2 = complex(4,5)

print(k1+k2)
print(k1-k2)
print(k1*k2)
print(k1/k2) 

b1=4.5
b2=7
b3=complex(b1,b2)
print(b3)

#%% Tuple data type
# Immutable (Degistirilemez)

liste1 =[1,2,3,5]
tuple1 =(7,8,-5,9)
print(liste1, tuple1)

liste1[0]=15

print(liste1, tuple1) # liste 0 elemanı degistirildi

# tuple1[0]=55 # 'tuple' object does not support item assignment error

# Tuple lar neden degistirilemez. İletilen verilerin degisitirlmemesini isteyebiliriz sadece okuma islemleri icin kullanırız. birden fazla veri tutan sadece return okunabilir yapan veri tipi

tuple2 = tuple("Ahmet")

print(tuple2) # Ahmet elemanları bir demet haline getirdi

tuple3 = tuple([2,1,8,9,10])
print(tuple3) # liste icindeki elemanları demet haline getirdi

tuple5 = tuple(["A","h","m","e","t"])

# elemanların sequence number vardir.

print(tuple5[1]) # index 0 dan baslıyor

#%% String data type karakter tutan veri tipi

# Immutable (Degistirilemez)

c1="F"
c2='F'

isim = "Fatih Kaan"
# isim ="Selim"
print("ALi Kaya") # immutable kaya --> kara olarak degistiremiyorz

isim = isim[:6]+ "Selim"
print(isim) # dolaylı yoldan degistirebiliyorz

# elemanların sequence number vardir.
print(isim[0])

# isim[0]="C" # 'str' object does not support item assignment error

#%% Range veri tipi 

aralik = range(0,10,1) # [0, 10) aralıgını tanımlar
print(aralik)
print(*aralik) # basına * koyarak o degerleri ulasabılırız

print(list(aralik)) # list cevirir
print(tuple(aralik)) # tuple cevirir

print(*range(1,15,3)) # 1 den 15e kadar 3 er 3 er yazıyor

print(*range(18,2,-5)) # 18 den 2 ye kadar -5 olarak azaltıyor

#%% tuple veri tipi. elemanları degistiirlemiyor

t1 =(15,25,17)
t2 = ("Ahmet","Mehmet")
t3 = (5+4j,"Melih",74.8,159) #1 farklı veri tiplerinden olusabilir
print(t3)

# t1[0]=1 # 'tuple' object does not support item assignment eleman degistiremiyoruz

t4 = tuple([10,20,32,14,26,65])
print(t4) # listeyi tuple demet haline getirdik

alltuple = t1+t2+t3+t4
print(alltuple) # tuple birleştirilebilir

# tuple elemanlarına erismek
print(t1[0])
print(t1[1:])

print(t4[2:])

print(t4[::2]) # 0 dan basla sonuna kadar git 2 ser yazdır
print(t4[0:len(t4):2]) # yukarıdakı yazımla aynı

print(t4[-1:0:-1]) # -1 yanı sondan basla 0 a kadar -1 er yazdır

# tuple metodları

t=(10,20,32,14,26,65,26,25,26)
print(t.count(26)) # tuple da 26 elemanını say

print(t.index(26)) # soldan sag 26 nın ilk index degerini verir

#%% sayi sistmei donusumu

print(bin(2)) # 2 lik tabanda yazımı bin--> binary 0b10 --> b--> binary tabanda anlamına geliyor

print(bin(19)) # 0b - binary 10011

# decimal
print(10) # 10 luk tabanda

# octal
print(oct(26)) # 0o- octal 32 

print(oct(8*8*8*8))

# hexadecimal

print(hex(368)) # 0x170 x hexadecimal karsılık geliyor 16 taban

print(hex(16*16*16))

#%% dizi lerde hazır fonksiyonlar

liste = [1,2,3,4]
tuple1 = (7,6,8,9)
set1={9,4,7,8,99}

print(sum(liste))
print(sum(tuple1))
print(sum(set1))

print(min(liste)) # min deger
print(len(tuple1)) # uzunlugunu veriyor
print(max(set1)) # e nyuksek deger

#%% list() mutable degisitirlebilr

liste = list([1,2,3,4,5])
liste1 = [2,6,5,99]
liste1[3]=100
print(liste1)

print(liste[0:len(liste):2])

isimler = ["Ahmet","Ali","Kaan"]

isimler =isimler + ["mehmet","Can"]
print(isimler)

isimler[0]="Yavuz"

print(isimler)

print(isimler[1:4:1])

isimler[1:4:1] = ["Ayse","Melek","Canan"]

print(isimler)


isimler = ["Ahmet","Ali","Kaan","Manolya"]
yaslar = [28,35,44,48]

karısıkliste= isimler + yaslar
print(karısıkliste)
karısıkliste.append(14.9) # liste sonuna obje ekler
# liste sonuna . koyarak ilgili fonksiyonlara ulasbiliriz

print(karısıkliste.index(28)) # 28 elemanın index degerini  verir

karısıkliste.pop() # liste sonundan elemen cıkarıyor indexte verebiliriz
print(" ************************* ")
print(karısıkliste)
print(karısıkliste.pop()) # liste sonundaki elemanı yazar cıkarılan eleman
print(karısıkliste)
karısıkliste.reverse() # tersten yazdırır
print(karısıkliste)

liste = [-5,6-88,-9]

liste.sort()
print(liste)

#%% cok boyutlu listeler

isimler= ["Fatih","Kaan","Selime","Oya"]
yaslar = [35,47,55,32]

bilgiler=[["Fatih",35],["Kaan",47],["Selime",55],["Oya",32]] # cok boyutlu liste 

print(bilgiler[0])
print(bilgiler[0][1])
print(bilgiler[1][0])

bilgiler = [({185:"Fatih"},{195:"Melek"}),("İstanbul","Denizli")]

print(bilgiler[0])
print(bilgiler[0][0][185])
print(bilgiler[0][1][195]) # set de id 185 olanın value ver diyoruz

print(bilgiler[1][1])


#%% set veri tipi
 # mutable degisitirlebilir elemanlar degisitirlebilir eleman sıra numaraıs yoktur. benzersizde deger ve anahtar yanı key  ve value degerler icirir . key kısmları benzersiz olmalıdır
 


set2 = {1,2,3,4,5,6}
set2.remove(4)
print(set2)

set3 = set([5,6,55,4,2,3,6,5,8,9,20])
print(set3)


# set motod ları . koyarak metodlara ulasabılırı set3.copy() vb. pratik yapılabilir


#%%  dictionary
# key ve value degelreri var key ile value ulasırız dict ya da {} dictionary olustururuz


sozluk = {1:"ALi",2:"Veli", "3 id": "Cuneyt"}
print(sozluk[1]) # key 1 olan value ALi dir

print(sozluk["3 id"])  # id istenilen sekilde verilebilir ama tutarlı olmak zorundadır

print(sozluk.get(2)) # 2 numaralı key sahip value getir

print(sozluk.get(3,"Bu anahtar sozlukte bulunmamaktadır "))# 3 numaralı key yoksa acıklama yazdırabiliriz

sozluk = {1:"Fatih",2:"Kaan",5:"Aliye"}

print(sozluk[5]) # sıra numarası yoktur anahtar numarasıyla value ulasırız
print(sozluk.get(2))

bossozluk = {}

bossozluk2 = dict()

anahtar = [1,2,3]
degerler = ["A","B","C"]
sozlukzip = zip(anahtar,degerler)
print(*sozlukzip) # zip leme basına * koy icindeki elemanları görmek icin
sozlukzip = zip(anahtar,degerler)
sozluk3 = dict(sozlukzip)
print(sozluk3[1])

keys=("Fatih","Kaan","Aliye")
values = ['Bilgisayar Mühendisi',
          'Elektronik Mühendisi',
          'Matematik Mühendisi']
yaslar = [1,2,3]
sozluk =zip(keys,values,yaslar)
print(*sozluk)

sozluk =zip(keys,values)
bilgiler =dict(sozluk)
print(bilgiler)

print(bilgiler["Kaan"])

#Sozlukte anahtar degeri yoksa ekleme yapar
bilgiler["Mehmet"]="Makine Mühendisi" # makine munedisi eklendi
print(bilgiler)

#Sozlukte anahtar degeri varsa guncelleme yapar
bilgiler["Mehmet"]="Doktor" # güncelleme
print(bilgiler)

# Silme
del bilgiler["Kaan"]
print(bilgiler)

# sozluk metodları
ogrenciler = {"Okan":"Makine ögrenmesi",
              "Armagan": ["Bilgisayar Agları","Dogal Dil İsleme"],
              "Kaan":["Makine Ogrenmesi","Dogal Dil işleme"],
              "Fatih":[{"Ders Adı": "Veri Tabanı", "Hoca": "Gülşah"}, {"Ders Adı": "Dogal Dil işleme","Hoca":"Burak"}]}

print(ogrenciler["Okan"])
print(ogrenciler["Fatih"][0]["Ders Adı"])
print(ogrenciler["Fatih"][0]["Hoca"])

o2= ogrenciler.copy() #  copy copya olusturur. clear bütün elemanların silinmesini saglıyor
print(o2)

# pop cıkarmak demek . diger function ları . ile cagırarak denenebilir































