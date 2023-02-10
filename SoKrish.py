Krish=[0,1,2,6,24,120,720,5040,40320,362880]
a = int(input())
for i in range(a):
    N = int(input())
    Check1=N
    Check=int()
    while(N>0):
        Check+=Krish[int(N%10)]
        N=int(N/10)
    if Check==Check1:
        print("Yes")
    else:
        print("No")
    