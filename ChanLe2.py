def check1(n):
    check=int()
    while(n>0):
        check+=int(n%10)
        n=int(n/10)
    if check % 10 == 0:
        return 1
    return 0

def check2(n):
    check = n % 10
    n = int(n/10)
    while(n>0):
        k = int(n % 10)
        if abs(int(check - k)) != 2 :
            return 0
        check = k
        n = int(n/10)
    return 1

a = int(input())
for i in range(a):
    b = int(input())
    if check1(b) == 1 & check2(b) == 1:
        print("YES")
    else :
        print("NO")

    