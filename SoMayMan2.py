def check(a):
    for i in range(len(a)):
        if a[i]!='4' and a[i]!='7':
            return 0
    return 1    
a=int(input())
while a>0 :
    b=input()
    if check(b)==1:
        print("YES")
    else : 
        print("NO")
    a-=1