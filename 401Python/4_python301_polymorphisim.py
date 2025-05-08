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











































