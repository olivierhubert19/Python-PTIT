import math
def isPrime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return x > 1
N,M = input().split()
N=int(N)
M=int(M)
a=[]
for i in range(N):
    K=input().split()
    K=[int(K[i]) for i in range(len(K))]
    a.append(K)
    

for i in range(N):
    for j in range(M):
        if(isPrime(a[i][j])==1):
            print(1,end=' ')
        else:
            print(0,end=" ")
    print()