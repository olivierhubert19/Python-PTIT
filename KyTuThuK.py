
Ans="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
T = int(input())
for t in range(T):
    N,K=map(int,input().split())
    S = (pow(2,N)-1)
    while N>0:
        if K == int(S/2)+1:
            print(Ans[N-1])
            break
        elif K>int(S/2)+1:
            N-=1
            S=int(S/2)
            K-=(S+1)
        else:
            N-=1
            S=int(S/2)