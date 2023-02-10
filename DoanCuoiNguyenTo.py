import math
def Check(N):
    if(N<2):
        return False
    if(N==2 or N==3):
        return False
    if(N%2==0):
        return False
    for i in range(2,int(math.sqrt(N))+1):
        if(N%i==0):
            return False
    return True
        
        
T = int(input())
for i in range(T):
    N=input()
    N=N[-4:-1]+N[len(N)-1]
    if(Check(int(N))):
        print("YES")
    else:
        print("NO")