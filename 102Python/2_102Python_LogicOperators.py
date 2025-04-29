#%% Karsılastırma operatorlerı
a=10
b=15
c=20
d=20

print(a==b)
print(c==d)
print(type(c==d))

print(a!=b) # esit değil true oluyor
print(c!=d)

print(a>b)
print(a<b)

print(c>=d)
print(d<=a)

print(f"{c>d}")

#%% Stringlerle karsılastırma
isim="Fatih"
print(isim=="Fatih")
print(isim!="Fatih")

print(isim=="Kaan")
print(isim!="Kaan")

# > sözlükte stringin sonra gelmesi
# < sözlükte stringin önce gelmesi

print("A">"B") # A B den sonramı geliyor
print("A"<"B") # A B Den öncemi geliyor

print("a">"B") # ASCI kodundna geliyor yanı 97 >66 mu dıye soruyor

# ASCII kodu sorgulama
print(ord("A"))
print(ord("B"))
print(ord("a"))

print("Ahmet">"Ayşe")

#%% Mantıksal Operatorler --> Birden fazla True falsın bırbırıne baglanmasıyla olusur
# or iki degerden en a birinin saglanması lazım sonuc 1 yada True cıkar
print(True or False)
print(1 or 0)

# and operatoru

print(1 and 0)
print(True and True)

# not operatoru True --> False False -->True olur

a=True
print("a ",a)
print("a ", not a)

#%% Ornekler

a, b = 10, 15

c, d, e = 20, 25, 30

print("OR")

print(a<15 or b<20)

print("AND")

print(a<15 and b<20 or a<15 and b>20)
print(not(a<15 and b<20 or a<15 and b>20))

# Tip donusumu

k1=4<5
k2 = 5>6
k3 = 7<=7

print(k1, k2, k3) # True ya da False dondururur

# üc deger de True doner. Her bir karakter oldugu icn True doner

sonuc1 = bool("Ahmet")
sonuc2 = bool(5)
sonuc2 = bool(4.8)


import sys
print(sys.getsizeof(5))# 5 ram deki memeory 28 karsılı kgleiyor
print(28*8) # 224 bitlik yer kaplıyor yanı 00000... 1111 gibi bir degerden olusuyor. 224 tane transistor 1 0 1 0 permutasyonlarıyla birlikte 5 karakterini olustuuryor

print(ord("A")) # A da 65 = 000.111 gibi 2 lk tabanda karsılıgı var bu skeilde A karakteri olusturuluyor

#%% Tek terimli operatorler
# + - ~

x=+---+12 # - + carpma olarak geliyor en sonda da pozitif mi negatif mi cıkıyor
print(x)

z=15
print(-----z)

# ~ operatoru bir sayının degilini almayı saglıyor bitwise operator

t=5 # ikilik tabanda 0101 karsılık gelir 0 işaret biti
# 0 ise sayı pozitif. 1 ise sayı negatig olduugnu anlıyorz

m=~t #(0101)' al =1010 olur isaret sol bastaki bir 1 o zaman sayı negatif.

# -A =A'+1 -> A' = -A - 1 = 1010 - 0001 = 1001
# A =(A')' = 0110 = onluk tabanda  -6 karsılık gelir
# o zaman 5 in degili 6 ya karsılık gelir
print(m)

#%% benzerlik operatoru
 
# is is not

x=5
y=5.0
print(x==y) # sadece degeri esitmi ona bakar
print(x is y) # hem tip hem deger eşit mi ona bakıyoruz

print(x is not y) # deger ve tip kontrolu
print(x!=y) # sadece degeri

#%% Üyelik operatorleri

# in      not in    eleman sorgulama 

kelime = "Türkiye"

print("ü" in kelime) #3 ü harfi kelimenin icinde var mı

print("ü" not in kelime) #3 ü harfi kelimenin icinde yok mu

print("ye" in kelime) #3 ye harfi kelimenin icinde var mı sıralama onemlı

print("Liste ici sorgu")
liste = [1,2,3]
print(1 in liste)
print(2 in liste)
print(3 in liste)
print(4 in liste)
print(4 not in liste)























