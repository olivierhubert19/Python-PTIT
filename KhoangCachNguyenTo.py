import math
def isPrime(x):
    if (x<2):
        return False
    if(x==2 or x==3):
        return True
    if x%2==0:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return True

Prime=[]
Prime.append(2)
Prime.append(3)
Prime.append(5)
Prime.append(7)
for i in range(11,10000,2):
    if isPrime(i):
        Prime.append(i)

print(len(Prime))

N,X = map(int,input().split())
print(str(X),end=" ")
for i in range(N):
    X+=Prime[i]
    print(str(X),end=" ")