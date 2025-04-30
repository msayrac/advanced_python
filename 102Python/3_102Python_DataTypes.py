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
























