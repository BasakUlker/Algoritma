def bastir(n):
    A = [1]
    fib1 = 0
    fib2 = 1
    i = 0
    for i in range(0,n):
        fib = fib1+fib2
        A.append(fib)
        fib1 = fib2
        fib2 = fib

    return(A)

n = int(input("Bir sayi girin:"))
B = []
B =  bastir(n)
for j in range(0,n):
    print(B[0:j+1])


