n = input("bir text girin:")
A = list(n)
B = []
for i in range(len(A)-1,-1,-1):
    B.append(A[i])

print(B)

