Test = int(input())
for i in range(Test):
    N = input()
    Check=1
    for i in range(0,len(N)-2):
        if N[i]!=N[i+2] or N[i]==N[i+1]:
            Check=0
            print("NO")
            break
    
    if Check==1:
        print("YES")