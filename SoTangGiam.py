def Check(a,i):
    Check1=i
    Check2=i
    while(Check1>=1):
        if(a[Check1]<=a[Check1-1]):
            return False
        Check1-=1
    while(Check2<len(a)-1):
        if(a[Check2]<=a[Check2+1]):
            return False
        Check2+=1
    return True

T = int(input())
for i in range(T):
    N =input()
    if(len(N)<3):
        print("NO")
    else:
        Check1=False
        for i in range(1,len(N)-1):
           if(Check(N,i)==True):
               Check1=True
               break
        if(Check1):
            print("YES")
        else:
            print("NO")
             