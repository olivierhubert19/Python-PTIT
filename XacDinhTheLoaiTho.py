N = int(input())
Tho=[]
for i in range(N):
    Tho.append(input().strip().split())
Ans=[1,2]
Res=[]
Res.append(Ans[len(Tho[0])%2])
Check=len(Tho[0])%2
if Check==1:
    Dem=1
else:
    Dem=0

for i in range(1,N):
    if(len(Tho[i])%2!=Check):
        Res.append(Ans[len(Tho[i])%2])
        Check=len(Tho[i])%2
    if len(Tho[i])%2==1:
        Dem+=1
        if Dem==4:
            Check=3
            Dem=0
    else:
        Dem=0
    
print(len(Res))
for i in Res:
    print(i)