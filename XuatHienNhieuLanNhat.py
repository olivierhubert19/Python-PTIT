T = int(input())
for t in range(T):
    A=input()
    A=[int(i) for i in input().split()]
    Check={}
    for i in A:
        if i in Check:
            Check[i]+=1
        else:
            Check[i]=1
    Key=0
    Max=0
    for key,val in Check.items():
        if val>Max:
            Max=val
            Key=key
        elif val==Max and key<Key:
            Key=key    
    if Max>int(len(A)/2):
        print(Key)
    else:
        print("NO")
    