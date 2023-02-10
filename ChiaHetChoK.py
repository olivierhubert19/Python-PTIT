
A,k,n = input().split()
a = int(A)
K = int(k)
N = int(n)
check1 = int(a/K)+1
check2 = int(N/K)
check = int()
for i in range(check1,check2+1):
    if(i*K>a):
        print((i*K-a),end=' ')
        check=1
if check == 0: 
    print(-1)