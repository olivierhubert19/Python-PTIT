import math

def isPrime(x):
    if (x<2 or x==4):
        return False
    if(x==2 or x==3):
        return True
    if x%2==0:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return True

N = int(input())
A = [int(i) for i in input().split()]
Ans = {}
for i in A:
    if i in Ans:
        Ans[i]+=1
    else:
        if isPrime(i):
            Ans[i]=1
for key,val in Ans.items():
    print(str(key)+" "+str(val))