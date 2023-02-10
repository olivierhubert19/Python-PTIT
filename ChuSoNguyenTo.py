from math import sqrt
def prime(n):
    if n<2:
        return False
    if n==2 or n==3:
        return True
    if n%2==0:
        return False
    for i in range(3,int(sqrt(n))+2,2):
        if n%i==0:
            return False
    return True

def Check(n):
    if prime(len(n)) == False:
        return False
    P=0
    NP=0
    for i in range(len(n)):
        if(prime(int(n[i]))):
            P+=1
        else:
            NP+=1
    if P<NP:
        return False
    return True

T = int(input())
for i in range(T):
    N = input()
    if Check(N):
        print("YES")
    else:
        print("NO")