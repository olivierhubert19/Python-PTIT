
b=int(input())
for i in range(b):
    n,x,m=input().split()
    N=float(n)
    X=float(x)
    M=float(m)    
    dem=int()
    while N<M:
        N*=(1+float(X/100))
        dem+=1
    print(dem)