#%% Inheritance

sayi = 5 # bu int sınıfından turemis

print(isinstance(sayi, int)) # sayi int sınıfının instance mi diye soruyor.
print(isinstance(sayi, float)) # sayi float sınıfının instance mi diye soruyor.

help(list) # list sınıfını detail bakabiliriz

print(issubclass(list,object)) # list sınıfı object sınıfının alt sınıfımı 

class A:
    pass

class B(A): # B sınıfı A sınıfını miras alıyor
    pass

class C(B): #C sınıfı B sınıfını miras alıyor
    pass

print(issubclass(B, A)) # B A nın subclass mı
print(issubclass(A, B)) # A B nın subclass mı
print(issubclass(C, A))

#%%

class A:
    def metod1(self):
        print("A Metod 1")
    def metod2(self):
        print("A Metod 2")
        
class B(A):
    def metod3(self):
        print("B Metod 3")
    def metod4(self):
        print("B Metod 4")

class C(B):
    def metod5(self):
        print("C Metod 5")
    def metod1(self):
        print("C Metod 1")
        
a1=A()
b1=B()
c1 =C()

print("****A sınıfı metodları****")
a1.metod1()
a1.metod2()
print("****B sınıfı metodları****")
b1.metod1()
b1.metod2()
b1.metod3()
b1.metod4()
print("****C sınıfı metodları****")
# C sınıfında metod1 oldugu icin ilk olarak C sınıfının metodunu calıstırır
c1.metod1()
c1.metod2()
c1.metod3()
c1.metod4()

print("mro --> metod resolution order")
# metod cozumlenme sıralaması ilk C sınıfına bakar yoksa B ye bakar yoksa A sınıfına bakar.
# birden fazla sınıflar miras alındıgında mro metodu işimizi kolaylastırır
C.mro()

# A A super class (parent class).
# B subclass (child class)

# B --> single level inheritance
# C --> B --> A multi level inheritance
# C -> (A,B) multiple level inheritance

#%% mro example

class X:
    def metod1(self):
        print("X metod 1")
    

class Z:
    def metod1(self):
        print("Z metod 1")

class Y:
    def metod1(self):
        print("Y metod 1")

class A(X,Y): # A X ve Y sınıfından miras alıyor multiple level
    def metod1(self):
        print("A metod 1")

class B(Y,Z):
    def metod1(self):
        print("B metod 1")

class C(B,A,Z):
    def metod2(self):
        print("C metod 2")

c1 = C()
c1.metod1()

print(C.mro()) # C sınıfından bir nesne uretildigi zaman hangi sıra ile metodları kullanıyor ona bakılır

#%% super fonksiyonu mıras alınan sınıflardan ilk sınıfın motodlarına ulasmayı saglayan bir fonksiyon

class D:
    def __init__(self):
        print("D constructor")
        
    def metot1(self):
        print("D metot 1")

class E:
    def __init__(self):
        print("E constructor")
    def metot1(self):
        print("E metot 1")

# F class D ve E inherit ediyor
class F(D,E):
    def __init__(self):
        print("F constructor")
    def metot1(self):
        print("F metot 1")
        super().metot1() # F nin ilk miras aldıgı  sınıfların metodlara da erisir. otomatik olarak D sınıfınn da metot1 cagırmıs oluruz
        super().__init__() # F nin miras aldıgı ilk sınıfın constructor cagırılır
        D.__init__(self) # D nin constructor u
        E.__init__(self) # E nin constructor ayrı ayrı calıstırılabılir
        

# constructor da F D ve E Seklinde calısır

f= F()
f.metot1()

print(F.mro()) # F class ile olarak F class sonra D class sonra da E class miras alıyor

#%% Inheritance Example 

# bir haber sitesinde haberler spor ve finans haberleri olmak üzere ikiye ayrılıyor.
# Her haberin baslıgı, icerigi ve bir adet gorseli bulunmaktadır
# Spor hareketlerinde video icerikleri de bulunmaktadır
# Finans haberlerinde doviz kurlarının bilgileride yer almaktadır

class Haber:
    def __init__(self,baslik,icerik,gorsel):
        self.baslik = baslik
        self.icerik = icerik
        self.gorsel = gorsel
    
    def bilgileriGoster(self):
        print("Main class func called")
        print(self.baslik,self.icerik,self.gorsel)

class Spor(Haber):
    def __init__(self,baslik,icerik,gorsel,video):
        super().__init__(baslik,icerik,gorsel)
        self.video = video        
        def bilgileriGoster(self):
            super().bilgileriGoster() # ana sınıftaki bilgileir goster
            print(self.video)
        def videoOynat(self):
            print(self.video,"isimli video oynatılıyor...")    
            

class Finans(Haber):
    def __init__(self,baslik,icerik,gorsel,dovizKurlari):
        super().__init__(baslik,icerik,gorsel)
        self.dovizKurlari = dovizKurlari
    def dovizKurlariBilgisiniGoster(self):
        for dovizAdi,dovizDegeri in self.dovizKurlari.items():
            print(dovizAdi, ":",dovizDegeri)
    
    def dovizKurlariniGuncelle(self,dovizKurlari):
        self.dovizKurlari = dovizKurlari 
                   
s1 = Spor(video="video1.mp4",baslik="Maçta kazanan olmadı",icerik ="0-0 bitti",gorsel="foto1.png")

s1.bilgileriGoster()

f1 = Finans(baslik="Ekonomi tüm dünyada durgun",icerik="Küresel salgın tüm dünyayı etkiledi",gorsel="foto2.png",dovizKurlari = {"Dolar":17,"Euro":18,"Sterlin":20})

f1.dovizKurlariBilgisiniGoster()

guncelKurBilgisi = {"Dolar":20,"Euro": 40, "Sterlin": 60}

f1.dovizKurlariniGuncelle(guncelKurBilgisi)

f1.dovizKurlariBilgisiniGoster()
