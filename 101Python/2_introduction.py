#%% cell 1
print("Hello World")


#%% cell 2
#  we use # symbol to make comment ctrl 1 or ctrl 4
# print("Python educaiton")

# control alt down arrow copy last and paste code clone upper arrow clone upper line

# clear in colsole--> clear console
# alt and arrow keys move the code. u can selct multiple code block to move it

print('İstanbul İzmir Ankara') # write in the same line

print("İstanbul") # write them in seperate line
print("İzmir")
print("Ankara")

# kaçış karakteri escape character write in the new line \n  or \t -- tab
print('İstanbul\nAnkara\nİzmir')

# tek tırnak "" or '' we can use \' 
print('Türkiye\'deki insanlar')

print("Türkiye'nin en güzel şehri \"İstanbul\"")


print("Python Eğitimi")
print("Python" + " "+ "Eğitimi") # combine two string using +

# raw string -- işlenmemiş string use r at the beginning içerisinde özel karakter yoktur anlamına geliyor raw string ters slah \ özel bir karakter alternatif olarak iki \\ da kullanabiliriz
print(r'C:\Users\lenovo\Desktop\Python2024Fall\İleriPython\101Python')

print('C:\\Users\\lenovo\\Desktop\\Python2024Fall\\İleriPython\\101Python')

# calcualtion + - * / % etc
print(5+6)
print(5*6)
print(5-6)
print(3**5) # üst alma

print(3.1 +4.2) # virgulden sonra sapmalar olabiliyor


# end paramtresi print icerisinde default olarak bulunmaktadır. İki print ifadesi yazarsak yeni bir satırda başlamasının sebebi
# end =\n
print("Python", end="\n")
print("Eğitimi")

print("Python", end=" *** ")
print("Eğitimi")

# sep = " "  seperator parameter

print("Hello", "World") # otomatik olarak bosluklar koyuyor
print("Hello", "World", sep="-")

print("Hello", "World","Awasome", sep="-", end="\n")

print(7,5,2025,sep="/")

print("Merhaba")
print(*"Merhaba", sep=".") # * iterator karakterleri tek tek yazdırıyor

# format method

print("İsim: Ali Can"
      "Soyadı: Kaya "
      "Doğum Tarihi: 01/01/1990")

# düzenli halde yazma iicn formate metodu kullanırız
print("Adı: {} Soyadı: {} Doğum Tarihi: {}".format("Ali Can","Kaya","01/01/1990"))
print("Adı: {} Soyadı: {} Doğum Tarihi: {}".format("Mehmet Efe","Kaya","01/01/1990"))

#TODO List istenilen bölümleri daha sonra yapabilmek icin ToDo list yapabiliyoruz

#TODO bu kısmı Ahmet yapacak


#TODO bu kısım 25 Mayıs a kadar bitirilecek
#TODO listeleri 

# binlerce satır kod yazdıgımızda istenilen TODO ulasmak icin
# source show todo list den bulabiliriz

#%% Help Fonksiyonu

help(print)

help(list)
# print üstüne çift tıklayıp control I basarsak print help ulasırız


#%%

# degiskenler icinde deger tutmayı saglayan gerektiginde degiskenin egerinin degismesini saglayan kavramdır.Bazı bilgilerin tutulması ve degismesini saglayan kavram 
# tüm deger tutan degiekenlere object denir.


sayi1=155 # integer
sayi2=167

# degisken isimlendirme print diye degisken olusturamayyız. anahtar kelime degisken atayamıyoruz

# print=10
# print(print)

# for
# def
# class
# while  özel anahtar kelimelerdir

# degisken isimlendirmeleri sayı ile baslayamaz

# 1deneme = 5
deneme1=5
print("1deneme".isidentifier()) #False
print("deneme1".isidentifier()) #True

# integer variable tam sayı degisken
sayi1=122
sayi2=57
print("Toplama : ", sayi1+sayi2)
print("Çıkarma : ", sayi1-sayi2)
print("çarpma : ", sayi1*sayi2)
print("Bölme : ", sayi1/sayi2)

type(sayi1) # integer
type(15.2) # float

print(id(sayi1)) # sayi 1 in RAM hangi adresinde depolandıgını  merak ediyorsak
sayi3 = 122
print(id(sayi3)) # sayi 3 in RAM hangi adresinde depolandıgını  merak ediyorsak yani int degerler aynı adreste depolanır


sayi3 = 144
print(id(sayi3)) # sayi 3 degesirse RAM da depoladıgı adres degisir

# float veri tipi kesirli veri tipi
print("Float veri tipi")
sayi1=10.2
sayi2=5.4
print("Toplama : ", sayi1+sayi2)
print("Çıkarma : ", sayi1-sayi2)
print("çarpma : ", sayi1*sayi2)
print("Bölme : ", sayi1/sayi2)

print(type(sayi1))
print(type(sayi2))


#%% str degiskeni

isim="Ali"
soyad = 'Kaya'

print(isim, type(isim),soyad,type(soyad))

print(len(isim)) # karakter uzunlugunu veriyor

print(isim, soyad, sep=" ") # defaul seperator bosuluk

print(isim + " " +soyad) # + concatenate eder
print("for")
for i in range(len(isim)):
    print(isim[i])
print("foreach")
for x in isim:
        print(x)

kelime ="Galata"
# kelime bas hargini degistirelim

# kelime[0]="S" # 'str' object does not support item assignment hatası alırız
# str ifadeler immutable --> degistirilemez
kelime="S"+kelime[1:]
print(kelime)

takim = "Galatasaray"
kelime1=takim[:6]
kelime2=takim[6:].capitalize()

print(kelime1)
print(kelime2)

yer = "istanbul"

print(yer[0::2]) # :: ikise atla demek
print(yer[0:len(yer):2]) ## bu skeilde de 2 ser atlama yapılır baslangı bitic ve adım sayısı

isim ="Kaan"
print(isim[::-1])# tersden yazdırma

#%% Objelerin RAM de ne kadar yer kapladıgı
# RAM heap bolgesınde depolanır
import sys # RAM de ne kadar yer kapladıgını gorme kıcın system kutuphanesini dahil edelim
sayi=1
print(sys.getsizeof(sayi))
isim="Python egitimi mi"
print(sys.getsizeof(isim))

# type conversion

x=6
y=5.8
z="185"

print(z*2)

print(int(z)*2)

# k="a125"
# print(int(k)*2) #◘ k ifadesini 10 luk tabanda int ceviremem

print(int(y))

print(17//6) # // bolmede int kısmı verir
print(17/6)
print(int(17/6)) # int kısmı verir

print(float(7))

print(float("16.2")*2)


#%% Kullanıcan input alma

girdi1 = input("lütfen bir kelime giriniz : ")

print("Girdiginiz kelime ", girdi1)

sayi1=int(input("Lütfen 1. sayiyi giriniz : "))

print("Girilen sayının 5 katı : ", 5*sayi1)

sayi2 = input("Lütfen 2. sayı giriniz : ")






























