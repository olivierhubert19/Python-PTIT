import math


def snt(n):
    if n == 2 or n == 3:
        return 0
    if n == 1 or n == 4:
        return 0
    if n%2==0:
        return 0
    for i in range(2,int(math.sqrt(n)),1):
        if n%i==0:
            return 0
    return 1
    
T = int(input())
for i in range(T):
    N=input()
    Check1=''
    Check2=''
    Check1=N[0]+N[1]+N[2]
    Check2=N[len(N)-3]+N[len(N)-2]+N[len(N)-1]
    if snt(int(Check1))==1 and snt(int(Check2))==1:
        print("YES")
    else: 
        print("NO")
    