#%% Karsılastırma operatorlerı
a=10
b=15
c=20
d=20

print(a==b)
print(c==d)
print(type(c==d))

print(a!=b) # esit değil true oluyor
print(c!=d)

print(a>b)
print(a<b)

print(c>=d)
print(d<=a)

print(f"{c>d}")

#%% Stringlerle karsılastırma
isim="Fatih"
print(isim=="Fatih")
print(isim!="Fatih")

print(isim=="Kaan")
print(isim!="Kaan")

# > sözlükte stringin sonra gelmesi
# < sözlükte stringin önce gelmesi

print("A">"B") # A B den sonramı geliyor
print("A"<"B") # A B Den öncemi geliyor

print("a">"B") # ASCI kodundna geliyor yanı 97 >66 mu dıye soruyor

# ASCII kodu sorgulama
print(ord("A"))
print(ord("B"))
print(ord("a"))

print("Ahmet">"Ayşe")

