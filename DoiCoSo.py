xchange="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def change(N,b):
    res=''
    while N>0:
        res=xchange[int(N)%int(b)]+res
        N=int(N/b)
    return res

for t in range(int(input())):
    N,b=map(int,input().split())
    print(change(N,b))