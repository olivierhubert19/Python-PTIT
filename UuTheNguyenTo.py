from math import sqrt
def Prime(n):
    if n<2:
        return False
    if n==2 or n==3:
        return True
    if n%2==0:
        return False
    for i in range(2,int(sqrt(n))+2):
        if n%i==0:
            return False
    return True

def chr(x):
    for i in x:
        if i not in ['2','3','5','7']: return False
    return True

T = int(input())
for t in range(T):
    N=input()
    if Prime(len(N))==False:
        print("NO")
    else:
        p=0
        np=0
        for i in N:
            if chr(i):
                p+=1
            else:
                np+=1
        if p>np:
            print("YES")
        else:
            print("NO")