name = str(input("Adınızı girin:",))
surname = str(input("Soyadınızı girin:",))

selamlama = print(f"Merhaba {name} {surname}. Yapmak istediğiniz işlem nedir? Neler yapabileceğiniz hakkında bilgi almak için B yazın eğer yapacağınız başka işlem yoksa exit yazın.")
istek = input()
def bilgi():
    print("İşte yapabileceğiniz işlemler bunlar:\n-Toplama\n-Çıkartma\n-Bölme\n-Çarpma")
def top():
    sayı = int(input(f"Kaç sayıyla işlem yapacaksın {name} {surname}?"))
    if sayı == 2:
        x = int(input("1. Sayıyı giriniz.",))
        y = int(input("2. Sayıyı giriniz.",))
        tsonuç = x+y
        print("Sonucunuz",tsonuç)
    elif sayı == 3:
        x = int(input("1. Sayıyı giriniz.",))
        y = int(input("2. Sayıyı giriniz.",))
        z = int(input("3. Sayıyı giriniz.",))
        tsonuç = x+y+z
        print("Sonucunuz",tsonuç)
    else:
        print(f"Malesef ki henüz {sayı} kadar işlem yapacak kapasitemiz yok.")
def fark():
    sayı = int(input(f"Kaç sayıyla işlem yapacaksın {name} {surname}?"))
    if sayı == 2:
        x = int(input())
        y = int(input())
        çsonuç = x-y
        print("Sonucunuz",çsonuç)
    elif sayı == 3:
        x = int(input("1. Sayıyı giriniz.",))
        y = int(input("2. Sayıyı giriniz.",))
        z = int(input("3. Sayıyı giriniz.",))
        çsonuç = x-y-z
        print("Sonucunuz",çsonuç)
    else:
        print(f"Malesef ki henüz {sayı} kadar işlem yapacak kapasitemiz yok.")
def böl():
    sayı = int(input(f"Kaç sayıyla işlem yapacaksın {name} {surname}?"))
    if sayı == 2:
        x = int(input("1. Sayıyı giriniz.",))
        y = int(input("2. Sayıyı giriniz.",))
        bsonuç = x/y
        print("Sonucunuz",bsonuç)
    elif sayı == 3:
        x = int(input("1. Sayıyı giriniz.",))
        y = int(input("2. Sayıyı giriniz.",))
        z = int(input("3. Sayıyı giriniz.",))
        bsonuç = x/y/z
        print("Sonucunuz",bsonuç)
    else:
        print(f"Malesef ki henüz {sayı} kadar işlem yapacak kapasitemiz yok.")
def çarp():
    sayı = int(input(f"Kaç sayıyla işlem yapacaksın {name} {surname}?"))
    if sayı == 2:
        x = int(input("1. Sayıyı giriniz.",))
        y = int(input("2. Sayıyı giriniz.",))
        çsonuç = x*y
        print("Sonucunuz",çsonuç)
    elif sayı == 3:
        x = int(input("1. Sayıyı giriniz.",))
        y = int(input("2. Sayıyı giriniz.",))
        z = int(input("3. Sayıyı giriniz.",))
        çsonuç = x*y*z
        print("Sonucunuz",çsonuç)
    else:
        print(f"Malesef ki henüz {sayı} kadar işlem yapacak kapasitemiz yok.")
if istek == ("B"):
    bilgi()
    print(f"Yapmak istediğiniz işlem nedir {name} {surname}?")
    işlem = input()
    if işlem == ("Toplama"):
        top()
    elif işlem == ("Çıkartma"):
        fark()
    elif işlem == ("Bölme"):
        böl()
    elif işlem == ("Çarpma"):
        çarp()
else:
    print(f"Tekrar görüşmek üzere {name} {surname}")
    




















