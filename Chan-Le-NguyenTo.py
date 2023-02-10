import math
def isPrime(x):
    if(x==2 or x==3):
        return True
    if x%2==0:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0: return False
    return x > 1

def Check(n):
    Ans=0
    for i in range(len(n)):
        if i%2==0 and int(n[i])%2!=0:
            return False
        if i%2!=0 and int(n[i])%2==0:
            return False
        Ans+=int(n[i])
    if isPrime(Ans):
        return True
    return False
            
T = int(input())
for t in range(T):
    N = input()
    if Check(N):
        print("YES")
    else:
        print("NO")