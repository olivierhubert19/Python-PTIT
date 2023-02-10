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

T = int(input())
for t in range(T):
    N = int(input())
    for i in range(13,N):
        if int(str(i)[::-1])<N and i<int(str(i)[::-1]):
            if Prime(i) and str(i)[::-1]!=str(i) and Prime(int(str(i)[::-1])):
                print(str(i)+" "+str(i)[::-1],end=" ")
    print()
