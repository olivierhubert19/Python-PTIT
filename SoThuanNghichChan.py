def Check1(n):
    n=str(n)
    for i in n:
        if int(i)%2==1:
            return False
    return True
def Ans(n):
    n=str(n)
    return int(n+n[::-1])
T = int(input())
for t in range(T):
    N = int(input())
    x = 2
    while True:
        if Ans(x)>=N:
            break
        if Check1(x):
            print(Ans(x),end=" ")
        x+=2
    print()