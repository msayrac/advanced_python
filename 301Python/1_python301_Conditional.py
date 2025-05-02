#%% if else statement birden fazla bilgi kontrol edilmesini saglar

# ornegin kullanıcı sifre ve kullanıcı adı girimini kontrol edebiliriz
# python da : bir blok actım anlamna gelir. yanı dort bosluk

if True or False:
    print("if bloguna girdi")

if 3<4:
    print("3<4")
elif 4<5:
    print("4<5")
else:
    print("Else bloguna girdi")
    

yas = 18

if yas <18:
    print("Reşit değilsiniz!")
else:
    print("Reşitsiniz!")  
    
sayi = 6
if sayi%2:
        print("{} sayısı tektir".format(sayi))
else:       
        print(f"{sayi} sayısı çifttir")

#%% finalden 50 altı alan kalıyor vize %40 final %60 ortalama <=50 gecer. vize 50 altı ise otomatik olarak kalıyor

vize=60
final=55

if final>=50:
    ort =0.4*vize + 0.6 * final
    if ort>=50:
        print("{} ortalamayla dersi gectirniz.".format(ort))
    else:
        print("ortalamanız {} kaldınız.".format(ort))
else:
    print(f"Final {final}<50 oldugu icin Kaldınız")
        
#%% pilotluk sınavında adayların ilk asamayı gecebilmeleri icin bir on kosul koyulmustur:
    # Kadın boy 1.60
    # Erkek boy 1.60
    # boy sınırını gectigi halde saglık muayenesini gecebilirler.
    
gender ="F"
boy =160

if gender=="F" and boy>=160:
    print("Ön saglık kontrolunu geçtiniz")
elif gender=="M" and boy>=170:
    print("Ön saglık kontrolunu geçtiniz")
else:
    print("Ön saglık kontrolunden elendiniz")
    
#%% Kullanıcıdan 3 tane sayı alan ve bu sayılardan en buyuk ve en kucuk degeri soyleyen degeri soyleyiniz

sayi1, sayi2, sayi3 = int(input("1. Sayı giriniz : ")),int(input("2. Sayı giriniz :")) ,int(input("3. Sayı giriniz : "))

print(sayi1, sayi2, sayi3)

buyuk= sayi1
kucuk = sayi1

if sayi1<sayi2 or sayi2 < sayi3:
    buyuk=sayi2
    if sayi2<sayi3:
        buyuk=sayi3
if sayi1>sayi2 or sayi1>sayi3:
    kucuk=sayi2
    if sayi2>sayi3:
        kucuk=sayi3
print("{} {} {} sayıları arasından kucuk olan sayı : {}".format(sayi1, sayi2, sayi3,kucuk))
       
print(f"{sayi1} {sayi2} {sayi3} sayıları arasından buyuk olan sayı : {buyuk}")       
        
#%% Kullanıcı adı ve sifre kontrolu yapan program

admin_username="admin"
admin_password="123"

username = input("Lütfen kullanıcı adını giriniz : ")
password = input("Lütfen şifrenizi giriniz : ")

if username==admin_username and password==admin_password:
    print("Sisteme basarılı sekilde giris yaptınız")
elif username==admin_username:
    print("Lütfen sifrenizi dogru giriniz")
else:
    print("Kullanıcı adı ve sifre yanlıs")

#%% Kenarları girilen ucgenin bilgisini soyleyen program

k1=20
k2=11
k3=30

if abs(k1-k2) < k3 and abs(k1+k2) > k3:
    if k1 == k2 and k1 == k3:
        print("Eşkenar üçgen")
    elif k1==k2 or k1==k3 or k2==k3:
        print("İkiz kenar ücgen")
    else:
        print("Çesitkenar ücgen")
else:
    print("Bu uc kenar bilgisiyle ucgen cizilemez")

#%% ASCII table --> bilgisayar alfabesi google ASCII yazıp karakterlere bakın

# A-Z 65- 90
# a-z 97-122

harf ="*"
# ord("a") girilen karakterin ascıı kodu ya da  unicode code of a specified character. 

if ord(harf)>=65 and ord(harf)<=90:
    print("{} Buyuk harf girdiniz".format(harf))
elif ord(harf)>=97 and ord(harf)<=122:
    print(f"{harf} kucuk harf girdiniz")
else:
    print("Girilen karakter '{}' latın alfabesinde bulunmamaktadır".format(harf))

print(ord("ç"))
print(ord("*"))
print(ord("="))
print(ord("?"))
