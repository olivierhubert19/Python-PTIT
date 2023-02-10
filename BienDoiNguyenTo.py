from math import sqrt

def prime(n):
    if(n<2): return False
    if(n==2 or n==3): return True
    if(n%2==0): return False
    for i in range(2,int(sqrt(n))+2):
        if(n%i==0):
            return False
    return True

Prime=[]
for i in range(2,10000+1):
    if(prime(i)):
        Prime.append(i)
print(Prime)
N = input()
A = [int(i) for i in input().split()]
Res=0
for i in A:
    if i not in Prime:
        Check=0
        while Prime[Check]<i:
            Check+=1
        if Check==0: Res+=1
        else: 
            Check=min(abs(i-Prime[Check]),abs(i-Prime[Check-1]))
            Res=max(Check,Res)
print(Res)

    
