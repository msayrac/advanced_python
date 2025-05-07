#%% OOP

# bir nesneyi tanımlıyoruz ve nesnenin sınıfını ortaya cıkarıyoruz. su ana kdar butun gorduklerımız objey idi bunlar bir sınıfa ait di.

# örnegin list sınıfını kullanarak liste int sınıfından integer tuple sınıfından tuple vb ürettik

# Yani sınıfta bir nesnenin ozellıkleri  ve metodları belirleniyor. sınıfla birlikte bir taslak ortaya cıkıyor. bız bu taslagı kullanarak ortaya objeler çıkarıyoruz

# insan ornegine bakacak olursak hepimizin eli sac rengi goz rengi yası adı tc boy kilo vb bilgilerimiz var bunlar birim yanı insan nesnesinin ozellıkleri oluyor. insans nesnesinin ozellıklerının birbirinden farklı olması ortaya sınıf kavramını cıkartıyor. Etrafımızda insanlar var ama her ınsanın ozellıklerı birbirindne farklıdır

# inheritence --> kalıtım
# Encapsulation --> Kapsülleme
# Abstraction --> Soyutlama
# polymorphisim --> çok çeşitlilik

# bir televizyon dedigimiz zaman aklımıza ne geliyor. bir tv nin özellikleri nelerdir fonksiyonları nelerdir

#Televizyon
    #üretim yeri
    #marka
    #model
    #Ekran boyutu
    #şekil
    #görüntü kalitesi
    #diger özellikler
    
    # ac/kapa
    # kana goruntuleme

#%% Python içerisinde hazır olarak gelen sınıflar

# tamsayılar int class türemis
a = 4

print(type(a))

print(type(5.5))

a=int(5) # int objesi uretiyoruz
b= float(7) # float objesi uretiyoruz

c="naber" # string class dan türüyor
print(type(c))

# her bir sınıfın kendi ozellıkleri var ve . ile cagırırız
c.capitalize() # string sınıfıın özelligi

#%% kendi sınıfımızı olusturalım

class Insan:
    #Attributes / property/ field/ variables/ özellikleri
    # behaviour / metodlar / fiileler / fonksiyonlar
    
    # ad, soyad, yas , meslek
    
    #constructor - yapıcı metod --> bır sınıfta nbır obje urettiginiz zaman cagırılan metoddur
    
    #constructor    
    def __init__(self):
        print("Constructor cagırıldı")
        pass
    
i1 = Insan() # insan constructorunu cagırıyorz initmetodu cagırıyorz      
i1.ad="Fatih"
i1.soyad="Karan"
i1.yas = 30
i1.meslek ="Bilgisayar Muhendisi"

i2=Insan()
i2.ad = "Mehmet"
i2.soyad="Can"
i2.yas=25
i2.meslek="Öğretmen"

# bir sınıftan iki tane obje instantiate - oluşturma

print(i1.ad,i1.soyad,i1.yas,i1.meslek)
print(i2.ad,i2.soyad,i2.yas,i2.meslek)

# tabi bir her insandan bir nesne olustururken uzun uzun ad soyad vb tanımlamamız gerekiyor mu. Cevap : Hayır

#%% sınıfn daha iyi anlasılır hale gelmesi biz sürekli her nesne icin ozellık tanımlaması yapamayız. yeri gelecek binlerce insans ya da nesne olusturmak zorunda kalacagız

class Insan:   
    
    def __init__(self,ad,soyad,yas,meslek):
        print("Constructor metodu her nesne olusturulduugnda cagırılır")
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.meslek = meslek
    
    # bir sınıf icin metod olusturma
    def bilgiSoyle(self):
        print("İnsanın Bilgileri")
        print(f"Adı Soyadı : {self.ad} {self.soyad} ")
        print("Yaşı : {}".format(self.yas))
        print("mesleği : {}".format(self.meslek))
        
        

i1= Insan("Fatih","Karan",30,"Bilgisayar Muhendisi")
i2= Insan("Mehmet","Can",25,"Öğretmen")

i1.bilgiSoyle()
i2.bilgiSoyle()

# ya da alternatif olarak
Insan.bilgiSoyle(i1)# Insan sınıfındaki bilgiSoyle fonksiyonunu i1 için cagırabilriz
Insan.bilgiSoyle(i2)

#%% Araba sınıfını modelleyelim

class Car:
    
    def __init__(self, brand,model,year,maintenance=True):
        self.brand=brand
        self.model=model
        self.year=year
        self.maintenance=maintenance
    
    def ozellikleriGoster(self):
        print(self.brand,self.model,self.year, end=" ")
        self.bakimDurumuGoster()
        
    def bakimDurumuGoster(self):
        if self.maintenance==True:
            print("Bakım yapılmış")
        else:
            print("Bakım yapılmamış")
        

# maintenance objede tanımlamıyorsak dogrudan True kabul edıyoruz
c1 =Car("BMW", "5.20", 2022)
c2 =Car("Ferrari", "P80/C", 2015,False)

c1.ozellikleriGoster()
c2.ozellikleriGoster()

c1.bakimDurumuGoster()
c2.bakimDurumuGoster()


c2 = Car(year=2017,maintenance=False, brand="Toyota",model="Corolla")
c2.ozellikleriGoster()
c2.maintenance=True
c2.ozellikleriGoster()

#%% variable çeşitleri
# Instance variable
# class/static variable

# sınıf ozellıklerı degiskenleri belirleyebiliyoruz

class User:
    # class namespace / variable
    sayac = 0
    
    def __init__(self,isim="isim yok",kayitTarihi="20.12.2020"):
        # object/Instance namespace
        User.sayac+=1 # kullanıcı olusturulunca sayac 1 artır
        self.isim=isim
        self.kayitTarihi=kayitTarihi

user1 = User("Mehmet Baki","01.05.2020")        
user2 = User("Ali Kara","06.04.2022")        

print(User.sayac) # class uzerindne sayaca ulasma
print(user2.sayac) # obje ustundende sayac ulasabılırız


#%% metot çeşitleri

# 1 - Instance (obje)) Methods
# 2 - Class Methods
# 3 - Static Methods


class Calisan:
    
    sirket="Turkcell" # her calısanın baglı olduug bir sirket vardır. calısan sınıfının ozelligi
    
    #constructor
    def __init__(self,isim,soyad,sabitMaas,prim):
        self.isim = isim
        self.soyad = soyad
        self.sabitMaas = sabitMaas
        self.prim = prim
    
    # obje Instance /  metodu metodda self cagırırız
    
    def toplamMaas(self): # self obje metodu yapıyor
        return self.sabitMaas + self.prim

    #class/ sınıf metodu
    @classmethod
    def sirketIsminiSoyle(cls): # cls ile bu kısmın sınıf metoduna ait oldugunu belirli ediyoruz        
        return cls.sirket

    # static method ne bir obje metodu ne de bir sınıf metodudur. parametresi / cls veya self tarafında parametresi olmayan metodları static metod deriz
    @staticmethod # python a sen bir static methodsun deriz yoksa self olarak alfılar
    def bilgi(info=None):
        
        if info!=None:
            print(info)
        else:
            print("Calisan sınıfına ait static bir metottur!")
    
c1 = Calisan("Aysel","Gündogan",5500,1750)
c2 = Calisan("Mehmet","Kasap",7500,1000)

print(c1.toplamMaas())

print(Calisan.toplamMaas(c2)) # Calisan sınıfından toplamMaas fonk cagır

#%% inner class

# sınıf ıcınde sınıf kullanmamızı kullanmamıza yarar

class Musteri:
    
    #constructor
    def __init__(self,musteriNo,isim,soyad,bakiye,hesapTuru):
        self.musteriNo = musteriNo
        self.isim = isim
        self.soyad = soyad
        # self.bakiye = bakiye
        # self.hesapTuru = hesapTuru
        self.hesap = self.Hesap(bakiye,hesapTuru)# musterimin hesap ozelligi artık bu sınıf içindeki hesap sınıfının kullanılmıs hali
    
    # object method
    def bilgileriGoster(self):
        print(self.musteriNo,self.isim,self.soyad)
        self.hesap.bilgileriGoster()
    
    class Hesap:        
        def __init__(self,bakiye,hesapTuru):            
            self.bakiye = bakiye
            self.hesapTuru = hesapTuru
        
        def bilgileriGoster(self):
            print("Hesap inner Sınıfından Bilgiler Getirliyor")
            print(self.bakiye,self.hesapTuru)
            
m1 = Musteri(1,"Selim","Kapı",5000, "TL")        
m2 = Musteri(2,"Ayse","Can",6000, "Dolar")        
      
m1.bilgileriGoster() 
m2.bilgileriGoster() 

euroHesap = Musteri.Hesap(8000, "Euro")

m1.hesap = euroHesap
m1.bilgileriGoster()


