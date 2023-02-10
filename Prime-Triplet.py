import math
def isPrime(x):
    if(x==2 or x==3):
        return True
    if x%2==0:
        return False
    for i in range(3, int(math.sqrt(x))+1,2):
        if x%i == 0: return False
    return x > 1

T = int(input())
for t in range(T):
    n = int(input())
    dem = 0
    for i in range(n-6):
        if (isPrime(i) and isPrime(i+2) and isPrime(i+6)) or (isPrime(i) and isPrime(i+4) and isPrime(i+6)):
            dem += 1
    print(dem)