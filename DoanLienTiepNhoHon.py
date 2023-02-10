T = int(input())
for t in range(T):
    N = int(input())
    A = [int(i) for i in input().split()]
    Ans=[]
    for i in range(N):
        while len(Ans)>0 and A[i]>=A[Ans[-1]]:
            Ans.pop()
        if len(Ans)==0:
            print(i+1,end=" ")
        else:
            print(i-(Ans[-1]),end=" ")
        Ans.append(i)
    del A