MOD=10**9+7
for t in range(int(input())):
    N,k=map(int,input().split())
    Val=""
    Res=0
    while k>0:
        if k%2!=0:
            Val=Val+'1'
        else:
            Val=Val+'0'
        k=int(k/2)
    for i in range(len(Val)):
        if Val[i]=='1':
            Res+=pow(N,i)
    print(Res%MOD)    