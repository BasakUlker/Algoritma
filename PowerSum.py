def kuvvet_bul(x):
    i = 1
    A = ["basak"]
    toplam = 0
    y = x

    while(x!=0):
        A.append(x-(x//10)*10)
        toplam = toplam + A[i]**4
        i+=1
        x = (x//10)
    if(toplam == y):
        return(y)
    else:
        return(404)


sayi = 9000
for i in range(9999):
    if( kuvvet_bul(sayi) == 404 and sayi != 9999 ):
        sayi+=1

else:
    print(sayi)



