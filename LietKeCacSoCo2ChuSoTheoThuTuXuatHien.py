n = input()
N = len(n)
if N%2==1:
    N-=1
Ans=[]
for i in range(0,N,2):
    A = n[i:i+2]
    if A not in Ans:
        Ans.append(A)
print(*Ans)