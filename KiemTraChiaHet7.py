def Check(n):
    if n==0:
        return 0
    for i in range(1000):
        if(n%7==0):
            return n
        n= n+int(str(n)[::-1])
    return -1

T = int(input())
for i in range(T):
    N = int(input())
    print(Check(N))