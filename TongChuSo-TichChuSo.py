a = int(input())
for i in range(a):
    N = input()
    tong=int()
    tich=1
    for i in range(len(N)):
        if(i%2==0):
            tong+=int(N[i])
        else:
            if int(N[i])!=0:
                tich*=int(N[i])
    if tich == 1:
        tich=0
    print("%d %d"%(tong,tich))