def tcs(n):
    tong=0
    while(n>0):
        tong+=int(n%10)
        n=int(n/10)
    return -int(tong)

T = int(input())
while(T>0):
    N = int(input())
    N = input().split()
    N = [int(i) for i in N]
    N.sort()
    N=sorted(N,key=tcs,reverse=True)
    for i in range(len(N)):
        print(N[i],end = ' ')
    print()
    T-=1