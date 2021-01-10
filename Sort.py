import random
import time

A = []

for i in range(10000):

    A.append(random.randint(1,101))

def quick_sort(x):

    if(len(x) == 1 or len(x) == 0):

        return (x)

    else:

        p = x[0]
        i = 0

        for j in range(len(x)-1):

            if (x[j+1] < p):

                x[j+1],x[i+1] = x[i+1], x[j+1]
                i += 1

        x[0],x[i] = x[i],x[0]

        ilk_kisim = quick_sort(x[:i])

        ikinci_kisim = quick_sort(x[i+1:])

        ilk_kisim.append(x[i])

        return (ilk_kisim+ikinci_kisim)

start = time.time()
Q = quick_sort(A)
end = time.time()

print("dizinin quick sort ile siralanma suresi:", start-end)

def bubble_sort(x):

    n = len(x)

    for i in range(n-1):

        for j in range(0, n-i-1):
            if x[j] > x[j+1] :
                x[j], x[j+1] = x[j+1], x[j]

start = time.time()
B = bubble_sort(A)
end = time.time()

print("dizinin bubble sort ile siralanma suresi:", start-end)

