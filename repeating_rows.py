
### 3 digit ile baslayalim:1,2,3. Sirayi takip eden satir kendinden onceki 3 satirin birlesiminden olusuyor. Bu kurala gore 100.satirdaki digitlerin toplamini bulan kod asagidaki gibidir###
### Her bir satirdaki digitlerin toplamlarini tutarak gidersek daha az yer kullanmis oluruz ve daha hizli sonuc aliriz:###

x,y,z = 1,2,3
row = 100 #hesaplanmasini istedigimiz satir


for i in range(row):
    x,y,z=y,z,x+y+z#bir sonraki satirdaki digitlerin toplamini hesaplayan satir

print(z)
