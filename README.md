# Pengertian Kondisi If Else If Bahasa Python
  Pada dasarnya, kondisi If Else If adalah sebuah struktur logika program yang di dapat dengan cara menyambung beberapa kondisi If Else menjadi sebuah kesatuan.
  Jika kondisi pertama tidak terpenuhi atau bernilai False, maka kode program akan lanjut ke kondisi If di bawahnya. Jika ternyata tidak juga terpenuhi, akan lanjut lagi ke kondisi If di bawahnya, dst hingga blok Else terakhir atau terdapat kondisi If yang bernilai True.


## yang pertama kita akan membuat contoh bilangan yang memasukin bilangan satu sampai tiga

  Bilangan1 = int(input("Masukkan Bilangan 1:"))
  Bilangan2 = int(input("Masukkan Bilangan 2:"))
  Bilangan3 = int(input("Masukkan Bilangan 3:"))

![pycharm](https://user-images.githubusercontent.com/56243690/68064451-40ec1180-fd4e-11e9-96e0-56a0af545ee7.PNG)


# Berikutnya kita juga bisa membuat kondisi if int(Bilangan1) and (Bilangan1 > Bilangan3): seperti dibawah ini :
 print("Nilai terbesarnya adalah :", Bilangan1)
    Terbesar = Bilangan1
    NomBil = "Bilangan 1"

![pycharm1](https://user-images.githubusercontent.com/56243690/68064487-c2dc3a80-fd4e-11e9-8132-8e4d0baac323.PNG)

# Selanjutnya kita juga bisa membuat kondisi elif (Bilangan2 > Bilangan3) and (Bilangan2 > Bilangan1): Seperti dibawah ini:
   print("Nilai terbesarnya adalah :", Bilangan2)
    Terbesar = Bilangan2
    NomBil = "Bilangan 2"

  else:
    Terbesar = Bilangan3
    NomBil = "Bilangan 3"
    
    ![pycharm2](https://user-images.githubusercontent.com/56243690/68064519-48f88100-fd4f-11e9-9505-ec6e2bd9c610.PNG)
    
# Selanjutnya menggunakan bilangan besar adalah
  print("Bilangan yang terbesar adalah", NomBil, "dengan nilai", Terbesar)
 
 
# Selanjutnya kita mengetahui setelah RUN yang benar:
![iftrue/false](https://user-images.githubusercontent.com/56243690/67921873-b2f01980-fbdb-11e9-82f4-7b145716d272.png)





 Pada if segment diatas memiliki ketentuan nilai if pertama harus bernilai true barulah nilai if yang berikutnya yang akan di proses atau dieksekusi, namun jika nilai if pertama bernilai false maka nilai if yang berikutnya tidak akan di proses, namun jika nilai if yang pertama bernilai true sedangkan nilai if yang kedua bernilai false maka yang akan di proses hanyalah if yang pertama. Berikut hasilnya jika if segment yang kita masukan bernilai true :
![iftrue/false](https://github.com/alviandwipramono/labspy02/blob/master/step.png)

selanjutnya kita juga bisa menambahkan is dan is not pada if segment seperti dibawah ini :

Pada Bahasa pemrograman python untuk membuat sebuah kondisi sama halnya dengan Bahasa pemgraman yang lain yaitu sama-sama menggunakan if, pada setiap pemrograman if berisi sebuah ekspresi logika menggunakan sebuah data yang telah dibandingkan seperti alur flowchart dibawah ini.

  Contoh:
  
![iftrue/false](https://user-images.githubusercontent.com/56243690/67922863-930e2500-fbde-11e9-9403-46022629cd60.png)



