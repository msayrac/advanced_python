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



















