N=int(input())
A = [int(i) for i in input().split()]
Check=0
for i in A:
    Check+=i
Check=int(Check/N)
Ans=0
for i in range(1,N):
    if abs(Check-A[i])<abs(Check-A[Ans]):
        Ans=i
Ans1=0
for i in range(N):
    Ans1+=abs(A[Ans]-A[i])

print(Ans1,A[Ans])