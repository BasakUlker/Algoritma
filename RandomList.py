#Random sayilardan olusturulan 100 elemanli dizideki ayni elemanlar silinir, her elemandan 1 adet kalir.
#A list is maden by random values from 1 to 100. Equal values is deleted, 1 of any and every values left.

import random
l=100
A = []
for i in range(100):

    A.append(random.randint(1,101))

    if(A.count(A[-1])>1):

        l=l-1

for j in range(0,l):

    x = A[j]

    if(A.count(x)>1):

        for k in range(A.count(x)-1):

            A.pop(A.index(x,A.index(x)+1))


print(A)


