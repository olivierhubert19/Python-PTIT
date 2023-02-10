def soSanh(A,B,N):
    for i in range(N):
        if A[i]>B[i]:
            return 0
    return 1

T = int(input())
for i in range(T):
    N = int(input())
    A=input().split()
    B=input().split()
    A=[int(i) for i in A]
    B=[int(i) for i in B]
    A.sort()
    B.sort()
    if(soSanh(A,B,N)==1):
        print("YES")
    else:
        print("NO")