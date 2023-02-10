from cmath import sqrt


def check(n):
    if n<2:
        return 0
    if n==2 or n==3:
        return 1
    if n%2==0:
        return 0
    for i in range(2,int(n/2),1):
        if n%i==0:
            return 0
    return 1
Test = int(input())
for i in range(Test):
    n = input()
    Check=''
    Check+=n[len(n)-4]
    Check+=n[len(n)-3]
    Check+=n[len(n)-2]
    Check+=n[len(n)-1]
    k = int(Check)
    if check(k) == 1:
        print("YES")
    else:
        print("NO")