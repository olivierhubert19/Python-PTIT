from math import sqrt
def snt(i):
    if i<2:
        return False
    for j in range(2,int(sqrt(i))+1):
        if i % j == 0:
            return False
    return True
def check(n):
    for i in range(len(n)):
        if snt(i)==True and snt(int(n[i])) !=True:
            return False
        if snt(i)!=True and snt(int(n[i])) ==True:
            return False
    return True
n = int(input())
for i in range(n):
    n=input()
    if(check(n)==False):
        print("NO")
    else:
        print("YES")    
    