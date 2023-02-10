n = input()
N = len(n)
if N%2==1:
    N-=1
Ans={}
for i in range(0,N,2):
    A = int(n[i:i+2])
    if A in Ans:
        Ans[A]+=1
    else:
        Ans[A]=1
for key,val in Ans.items():
    print(key,val)