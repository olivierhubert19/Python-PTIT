for t in range(int(input())):
    N = int(input())
    A= [ int(i) for i in input().split() ]
    A.sort()
    tong = 0
    for i in range(1,N):
       if(A[i]>A[i-1]): tong+=(A[i]-A[i-1]-1)
    print(tong)