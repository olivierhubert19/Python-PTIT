N = int(input())
A = [float(i) for i in input().split()]
N=len(A)
A.sort()
Tong = 0
Fisrt=A[0]
Second=A[len(A)-1]
for i in A:
    if i == Fisrt or i ==Second:
        Tong-=i
        N-=1
    Tong+=i

print(round(Tong/N,2))