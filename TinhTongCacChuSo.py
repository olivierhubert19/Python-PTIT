T = int(input())
for t in range(T):
    S = input()
    Check=0
    Ans=[]
    for i in S:
        if i>='A' and i<='Z':
            Ans.append(i)
        else:
            Check+=int(i)
    Ans.sort()
    for i in Ans:
        print(i,end='')
    print(Check)