#%% polymorphisim poly --> çok demek morph --> biçim. Yani çok bicimlilik demek anlamına geliyor

# ornegin at ses cıkarır kus da ses cıkarır

# araba ve motorun calısma bicimi farklı ama davranıs olarak aynı. bu farklılıklar aynı metodun farklı davranıslar gostermesıne polymorphism denir

class Arac:
    
    def __init__(self,tur):
        self.tur = tur
        
class Araba(Arac):
    def __init__(self):
        super().__init__("Araba")
        
    def calis(self):
        print("Motor calıstı.")
        print("Hareket etmeye baslayabilirsin!")

class Motorsiklet(Arac):
    def __init__(self):
        super().__init__("Motorsiklet")
    
    def calis(self):
        print("Motor çalıştı.")
        print("Motor ısınmaya basladı.")
        print("Motor ısınma süreci bitti.")
        print("Hareket etmeye baslayabilirsin.")


a1 = Araba()

m1 = Motorsiklet()

a1.calis()
m1.calis()



class Insan():
    
    def git(self,arac : Arac): # arac parametresi icin Arac objesi kullan diyoruz
        arac.calis()
        print("Hareket etmeye basladıgım aracın turu : ", arac.tur)

print(10*"*")
i1 = Insan()
i1.git(m1)
print(10*"*")

#%% Operator overloading --> aşırı yüklenmesi

# bir fonksiyonun birden fazla is ifarklı parametrelerle yapması anlamına geliyor

sonuc = int.__add__(20,30)
print(sonuc)

print(20+30)

print(str.__add__("Galata","saray"))
print("Galata"+"saray")

#%% magic metods --> büyülü metodlar

print(int.__sub__(5,2))
print(int.__mul__(5,2))

print(int.__truediv__(5,2))
print(int.__divmod__(5,2)) # bolumu ve kalnı tuple olarak verir
print(int.__mul__(5,2))

#%% metod overloading ve metod overriding
# metod overloading
def topla(s1,s2):
    return s1+s2

def topla(s1,s2,s3=0): # s3 =0 default assign ederek metod overloading gerceklestiriyoruz
    return s1+s2+s3
    
print(topla(2,3))
print(topla(2,3,5))

# metod overriding

class Bina:
    def __init__(self,binaNo):
        self.binaNo = binaNo
    def adresSoyle(self):
        print("No : ",self.binaNo)

class Daire(Bina):
    
    def __init__(self, daireNo,binaNo):
        self.daireNo = daireNo
        super().__init__(binaNo)
    #metod overriding metodun gecersiz kılınması
    def adresSoyle(self):
        print(f"Bina No : {self.binaNo} Daire No : {self.daireNo}")
        
b1 = Bina(68)
d1 = Daire(7,b1.binaNo)

d1.adresSoyle()

#%% abstraction soyutlama

# her makinenin bir calısma davranısı var













































