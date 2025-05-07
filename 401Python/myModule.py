from math import pi

def topla(a,b):
    return a+b

def daireCevreHesapla(r):
    return 2*pi*r



def daireAlanHesapla(r):
    """
    Parameters
    --------
    r: dairenin yarıçapı
    returns
    --------
    Dairenin alanının bilgisini verir.    
    """
    return pi*r*r

# main hangi dosya calıstırıyorsa name == main oluyor
if __name__ == "__main__":
    print(topla(3,6))


print(__name__)