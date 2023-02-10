T = int(input())
for t in range(T):
    n,m = map(int,input().split())
    X = [int(i) for i in input().split()]
    Check=0
    Am=[]
    Duong=[]
    for i in range(1,len(X)):
        if X[i]>X[Check]:
            Check=i
    X.insert(Check,m)
    for i in X:
        if i<0:
            print(i,end=" ")
    for i in X:
        if i>=0:
            print(i,end=" ")
    print()
        