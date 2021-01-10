def asal_kontrol(x):
    p = int(x**(1/2)//1)
    if(x%2==0 and x != 2):
        return(0)
    for i in range(3,p+1):
        if(x%i==0 and x != i):
            return(0)
    return(1)

n = int(input("bir sayi girin:"))

if(asal_kontrol(n)==1):
    print("sayi asaldir.")

else:
    print("sayi asal degildir.")

