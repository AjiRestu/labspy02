Bilangan1 = int(input("Masukkan Bilangan 1:"))
Bilangan2 = int(input("Masukkan Bilangan 2:"))
Bilangan3 = int(input("Masukkan Bilangan 3:"))

if int(Bilangan1) and Bilangan1 > Bilangan3:
    print("Nilai Terbesarnya adalah :", Bilangan1)
    Terbesar = Bilangan1
    NomBil = "Bilangan 1"
elif (Bilangan2 >Bilangan3) and (Bilanga2 > Bilangan1):
    print("Nilai terbesarnya adalah :", Bilangan2)
    Terbesar = Bilangan2
    NomBil = "Bilangan2"
else:
    Terbesar = Bilangan3
    NomBil = "Bilangan 3"

print("Bilangan yang terbesar adalah", NomBil, "dengan nilai", Terbesar)
