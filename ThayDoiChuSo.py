def INT(n):
    sum = 0
    mu = 1
    for i in range(len(n)-1,-1,-1):
        sum+=mu*n[i]
        mu*=10
    return sum

T = int(input())
for t in range(T):
    p,q = input().split()
    p=int(p)
    q=int(q)
    
    Check = 2
    N=[]
    while Check>0:
        data = input()
        for i in data.split():
            N.append(i)
        Check-=len(data.split())
        
    X1=N[0]
    X2=N[1]    
    X1 = [int(i) for i in X1]
    X2 = [int(i) for i in X2]
    
    for i in range(len(X1)):
        if X1[i]==p:
            X1[i]=q
    for i in range(len(X2)):
        if X2[i]==p:
            X2[i]=q
    first = INT(X1)+INT(X2)
    
    for i in range(len(X1)):
        if X1[i]==q:
            X1[i]=p
    for i in range(len(X2)):
        if X2[i]==q:
            X2[i]=p
    second = INT(X1)+INT(X2)  
    
    if first<second:
        print(str(first)+" "+str(second))
    else:
        print(str(second)+" "+str(first))    
         
        