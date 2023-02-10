T = int(input())
while(T>0):
    N=input()
    N=[int(N[i]) for i in range(len(N))]
    for i in range(len(N)-1,0,-1):
        if(N[i]>=5):
            N[i]=0
            N[i-1]+=1
        else:
            N[i]=0
    if(N[0]==10):
        N[0]=0
        print(1,end="")
    for i in N:
        print(i,end="")
    print()
    T-=1