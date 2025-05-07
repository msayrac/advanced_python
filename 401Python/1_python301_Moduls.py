#%% Modules
# Modul su ana kdar math functool time modulu kullandık
# programlarımız yazmad aislerimiz kolaylatırı arkadalar
# biz time modulu icinde  time fonk kullandık
# bu fonk  1 ocak 1970 de beri gecen sanıyenın bilgisini veriyo bize
# biz bu kodu yazmak zamanımızı alır bu sebeple hazır kutuphaneleri kullanıyoruz

# bu moduler dogrudan python enterpreter dahil edilmis builtin module diyoruz c dile ile yazılmıs. Python icindeki builtin modulleri merak ediyorsak bu modulleri gorebiliyirz

import sys
print(sys.builtin_module_names)

#%% kendi modullerimiz hazırlayabiliriz
# yeni bir dosya olsuturalım adını myModule.py verelim. module icine topla fonksiyonu tanımlayalım

# import sys
# print(sys.path)

# import myModule
# print(myModule.topla(5, 6))
# print(myModule.daireCevreHesapla(5))

# ya da 
# from myModule import topla # sadece kullanılacak module cagrabiliriz modul ismini kullanmayız
# print(topla(5, 6))
# # print(daireCevreHesapla(5))

# ya da * ile myModule icindeki tum fonk cagırırız

from myModule import * # tüm moduller cagırılır
print(topla(5, 6))
print(daireCevreHesapla(5))
print(daireAlanHesapla(3))

#%% __name__ degiskeni python degiskeninde hazır degiskenlerden __name__ karsılıgı main ana temel demek
# ana klasor salısıyor demek

# print(__name__)

# myModule icinde de print(__name__) diyelim
# myModule cagırdıgımda 
from myModule import *
# print(__name__)

#%% func dokumantasyona hazırlama
# """ """ ile myModule icindek fonksiyonu acıkıklama yapabiliyoruz. Bu sayede documantasyonlar modulu kullanımı daha kolay oluyor
import myModule

myModule.daireAlanHesapla(3)
myModule.daireCevreHesapla(1)

#%% istersek modulleirn ismini kısaltabiliyoruz as diyerek

import myModule as mm

mm.topla(5, 6)














