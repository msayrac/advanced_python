#%% Loops algoritman覺n defalarca yap覺lmas覺n覺 saglar

for i in range(1,5):
    print(f"{i}. yaz覺 --> Hello Python")

# foreach loop
print(*range(5,10)) # [5,10)
for sayi in range(5,10):
    print(sayi)

liste=["Ahmet","Mehmet","Hasan","Kamil","Selin"]

for isim in liste:
    print(isim)

for isim in liste:
    for letter in isim:
        print(letter)

tup = (5,"ahmet",{12:"Kemal"})
for i in tup:
    print(i)

print(tup[2][12])

#%% while loop

# baslang覺c ve bitisde for loop
# baslang覺 ve biti yoksa while loop

i=1 # initialisation
while i <= 5:
    print(i)
    i+=1

#%% example

sayilar = [10,20,30,40,50,60]
i=0

while i < len(sayilar):
    print(sayilar[i])
    i+=1

print("Reverse order ")
i= len(sayilar)-1

while i>=0:
    print(sayilar[i])
    i-=1

#%% example 1 den 20 kadar olan say覺lar覺n toplam覺

sayi = 1
toplam =0
while sayi<=20:
    toplam+=sayi
    sayi+=1
print(f"[1-20] aras覺ndaki say覺lar覺n toplam覺 : {toplam}")

#%% 2 say覺 aras覺ndaki 5 ve 7 ye bolunebilen say覺lar覺 yazd覺ran program

start = 1
finish = 26

for i in range(start,finish):
    if i%5==0:
        print(f"{i} say覺s覺 5 e bolunur")
    elif i%7==0:
        print("{} say覺s覺 7'ye bolunur".format(i))

start = 1
finish = 100
count=0
while start<=finish:
    if start%5==0 and start%7==0:
        print(start)
        count+=1
    start+=1
print(f"5 ve 7 ye bolunebilen {count} adet say覺 vard覺r")


#%%
"""
sek覺ldek覺 c覺kt覺y覺 ekrana yazd覺ran program覺 yaz覺n覺z
$$$$$$$$$$
$$$$$$$$$$
$$$$$$$$$$
$$$$$$$$$$
$$$$$$$$$$
$$$$$$$$$$
$$$$$$$$$$
"""
for i in range(8):
    print(10*"$")

print(" **************  ")
satir=0
satir_sayisi = 7
sutun_sayisi = 10
while satir<satir_sayisi: # sat覺r
    sutun=0
    while sutun<sutun_sayisi: # s羹t羹n
        print("$", end="")
        sutun+=1
    print() # bir alt sat覺ra gecmesi icin
    satir+=1

#%% girilen say覺n覺n say覺 degerlerinin toplam覺n覺 bulan program

num=785
temp = num
total=0
sayi_deger= []
while temp>0:
    total += temp%10
    sayi_deger.append(temp%10)
    # temp = int(temp/10)
    temp//=10
sayi_deger.reverse()
print(f"{num} say覺s覺n覺n say覺 degerleri toplam覺 : {total}")   
print("{} say覺s覺n覺n say覺 degerleri : {}".format(num,sayi_deger))   

#%% factoriel hesab覺

n = 1
if n>=0:
    i=1
    fact = 1
    while i <= n:
        fact*=i
        i+=1
print(f"{n}! = {fact}")

#%% for loop in detail 

for karakter in "Fatih Kaan":
    print(karakter)

sayilar = [2,6,55,6]
for sayi in sayilar:
    print(sayi)

bilgiler = {"Fatih":"Bilgisayar Müh.","Kaan":"Kimya Müh.","Aliye":"Matematik Müh"}

# elemanları yazdırır key degerleri
for key in bilgiler:
    print(key)
    
# bilgiler.keys() aynı seydir 
for key in bilgiler.keys():
    print(key)

for value in bilgiler.values():
    print(value)
# aynı seydir
for key in bilgiler:
    print(bilgiler[key])

# hem key hem de value nasıl ulasırız

print(bilgiler.items())

# ikiserli olarak getirir bilgiler.items()
for eleman in bilgiler.items():
    print(eleman)

# pateki acarak da yazdırabiliriz

for key, value in bilgiler.items():
    print("Adı : ", key, "Meslegi : ", value)
    
#set objesi

benzersiz_sayilar = {2,3,4,55,6,98,87,5,5} # benzersiz elemanları yazdırır
print(benzersiz_sayilar)   
    
for sayi in benzersiz_sayilar:
    print(sayi)

#tuple
print("tuple listesi")
tuplelistesi = [(21,51),(41,54),(-5,4),(-5,-9)]

for ikili in tuplelistesi:
    print(ikili)

print("tuple elemanları ayrı yazdırma")
for ikili in tuplelistesi:
    sayi1, sayi2 =ikili
    print(sayi1,sayi2)
    
print("tuple elemanları ayrı yazdırma")
for sayi1, sayi2 in tuplelistesi:
    print(sayi1, sayi2)


tuplelistesi = [("Okan",25,1578),("Melike",35,957)]    
oyuncuNumarasi =1
for ad, yas, puan in tuplelistesi:
    print(f"{oyuncuNumarasi}. Oyuncunu Bilgileri")
    print("Ad : ",ad)
    print("Yaş : ",yas)
    print("Puan : ",puan)
    oyuncuNumarasi+=1
    
#%% for loop example
# liste icindeki tek ve cift sayıları kac tane olduugnı bulalım
sayilar = [2,3,4,5,6,99,4,5,2,1,88,9,78]

tekSayilar =[]
ciftSayilar = list()

for sayi in sayilar:
    if sayi%2==0:
        ciftSayilar.append(sayi)
    else:
        tekSayilar.append(sayi)
    
print("Tek Sayılar : {} ve adet : {}".format(tekSayilar, len(tekSayilar)))
print(f"Çift Sayılar : {ciftSayilar} ve adet : {len(ciftSayilar)}")
    
#%%  10*10 tabloda carpma islemi yapalım
"""
1*1  1*2                     1*10



10*1  10*2                   10*10=100
"""

for row in range(1,4):
    for column in range(1,4):
        print(f"{row}x{column} = {row*column}","\t", end="")    
    print()
    
#%% 1 -500 arasi sayıların karekökü tamsayı olan sayıları bulan program

from math import *

for i in range(10):
    if int(sqrt(i))**2 == i:
        print(f"Karekök {i} = {int(sqrt(i))}.  {i} karekökü tam sayı olan sayıdır.")

#%% break continue ve pass anahtar kelimeleri

# break karsılasınca dongunun kıırlmasını saglar
# kosul saglanınca dongu kırılır

# 5 e eşit olunca donguyu kırar 5 e kadar olan sayıları yazdırır
for i in range(10):
    if i==5:
        break
    print(i)




sayi=10
while True:   
    print(sayi)    
    if sayi==20:
        break
    sayi+=1
print("Dongu Kırıldı") 

# continue --> dongunun devamını saglar
# 5 e bolunemeyen sayıları ekrana yazdır
for sayi in range(20):
    if sayi % 5 !=0:
        print(sayi)

# continue gelince bir sonraki etapa gecis yapar
# 5 e eşit olunca 5 i yazdırmaz bir sonraki adıma gecer
for i in range(10):
    if i==5:
        continue
    print(i)

for sayi in range(20):
    if sayi % 5 ==0:
        continue
    print(sayi)

i=0
while i<5:
    if i==3:
        i+=1
        continue # continue denenebilir
    print(i)
    i+=1
    

# pass pass gecmek

for i in range(10):
#TODO bu kısmı pass gecildi gerekli fonksiyonlar eklenecektir
    pass # bu blok pass gecilebilir sonra dolduracagım

print("Baska islemler yapılacaktır")

if i==0:
    pass # ne yapacagımızı bilmiyorsak pass gecebiliriz
elif i==1:
    pass # pass bos bir satır hıc bır ıse yaramıyor bu blok doludur ya da dolacaktır anlamına geliyor

#%% break example
# bir string icindeki karakterin index degerini bulmak

isim = "Kemal Can Karpuz"
aranacakHarf= "a"
index=0
for karakter in isim:
    if karakter ==aranacakHarf or karakter==aranacakHarf.upper():        
        print(f"{aranacakHarf} harfi {index}. index te bulunmaktadır.")
        break
    index+=1


#%% enumerate fonksiyonu

# enumerate fonksiyonu bir dizinin icindeki elemanların sıralanmasını saglayan. Yani sıra numarası vermemizi saglayan fonksiyondur

isim= "Galatasaray"

# isim icindeki harflerin sıra numarasını yazdırmak istiyorum

# normalde index = 0 olarka belirlyip yapıyorduk ornegin
index=0
for harf in isim:
    print(f"{harf} harfi {index}. indexte bulunmaktadır")
    index+=1

# bunun yerine  kalıcı ıslemler ıcın enumerate fonksiyonu ısımıız kolaylastırıyor
print(isim)
print(*enumerate(isim))
print(list(enumerate(isim)))
 
# bu sekilde her bir harfi numaralandırmıs oluyoruz.  tuple olarak depolıyor

print(list(enumerate(isim,7))) #• numaralandırmayı 7 den baslatır

for index,harf in enumerate(isim):
    print(index,harf)
    print(f"{harf} harfi {index}. indexte bulunmaktadır")
    
#%% enumerate ornek

isim = "Fatih Karan"

for index, harf in enumerate(isim.lower()):
    if harf =="a":
        print(f"{harf} harfi {index}. indexte bulunmaktadır")

liste = ["a",5, True,7.5]

for index, value in enumerate(liste):
    print(index, value)

#%% Exp. kullanıcı giris bilgilerini dogru girdigi takdirde istedigi kadar sayı girebilmesini ve bunları kucukten buyuge sıralanmasını saglayan programı yazdırınız

# username= hesap sifre=123
username ="hesap"
password="123"

while True:
    _username ="hesap"
    _password="123"
    
    if username != _username:
        print("Sistemde boyle bir kullanıcı bulunmamaktadır")
    elif  password != _password:
        print("Parolanıız yanlıs girdiniz")
    else:
        sayiAdeti=int(input("Lütfen sayı adeti giriniz : "))
        sayilar=[]
        for i in range(sayiAdeti):
            sayi=int(input(f"{i+1}. sayi giriniz : "))
            sayilar.append(sayi)
        sayilar.sort(reverse=True)# buyukten kucuge sıralar
        for sayi in sayilar:
            print(sayi, end=" ")
        print()
        break


