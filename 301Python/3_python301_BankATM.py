#%% ATM example
# Kartın bir şifresi vardır
# Kartın baslangıc bakiyesi 500tl dir
# 3 defa sifre yanlıs girilince kart bloke olacaktır
# ATM'nin işlem menüsünde para çekme, para yatırma, bakiye sorgulama ve kart iade işlemleri yapılmaktadır

_kartSifre = "123" # bu aslında banka veri tabanında kayıtlı olan sifredir.
_bakiye = 500 # katın ilk bakiyesi
sifre_sayac = 3

login=False


while True:
    if login==False:
        sifre=input("Lütfen sifrenizi giriniz : ")
    if sifre==_kartSifre:
        login=True
        print("""
            1. print("Para Çek") 
            2. print("Para Yatır") 
            3. print("Bakiye Sorgula") 
            4. print("Kart İade")         
              """)
        secim =int(input("Hangi işlemi yapmak istiyorsunuz : "))
        if secim == 1:
            miktar =int(input("Kac para cekmek istiyorsunuz : "))
            if _bakiye < miktar:
                print("Yeterli bakiyeniz bulunmamaktadır.")
                continue
            if _bakiye>=miktar:
                _bakiye -= miktar
                print("Çekilen tutar {} Tl".format(miktar))
                print(f"Kalan bakiyeniz : {_bakiye}")
        elif secim == 2:
            miktar = int(input("Kaç Tl yatırmak istiyorsunuz"))
            _bakiye +=miktar
        elif secim == 3:
            print(f"Bakiyeniz {_bakiye} TL")
        elif secim == 4:
            print("Yine bekleriz")
        else:
            print("Lütfen 1-4 arası secim yapınız!")            
    else:
        sifre_sayac-=1
        if sifre_sayac <=0:
            print("Kartınız bloke olmuştur! Lütfen banka ile iletişime geciniz.")
            break
            
#%% for else döngüsü
# çift sayı bulan program

sayilar = [3,7,11,20,22]

for sayi in sayilar:
    if sayi % 2 == 0:
        print(f"{sayi} çift sayıdır")
        break # break gormezse else icine girer.        
else:
    print("çift sayı bulunmamaktadır!")
        
#%% for dongusunun kullanıldıgı yerler

sayilar = [-2,0,11] # bu sayıların karesini merak ediyoruz
sayiKareleri = []
for sayi in sayilar:
    sayiKareleri.append(sayi**2)
print(sayiKareleri)  
           
print("sayilarinKaresi2")
sayilarinKaresi2 = [x*x for x in sayilar] # sayıların icinde gezin x olarka ve sayıların karesini al. for bu skeilde de kullanılıyor
print(sayilarinKaresi2)   

print("sayilarinKaresi3") # tuple olarak da olusturulabilir  
sayilarinKaresi3 = tuple(x*x for x in sayilar)
print(*sayilarinKaresi3)

sayilarinKaresi3 = tuple(sayilarinKaresi3)
print(sayilarinKaresi3)

print("sayilarinKaresi4") # set olarak da olusturulabilir  
sayilarinKaresi4 = set(x*x for x in sayilar)
print(sayilarinKaresi4)
print(*sayilarinKaresi4)

