N = int(input())
a=input().split()
a=[int(i) for i in a]
check = 0
while(check<N-1):
    if (int(a[check])+int(a[check+1]))%2==0:
        del(a[check])
        del(a[check])
        N-=2
        if check > 0:
            check-=1
        else:
            check = 0
    else :
        check+=1
print(N)    
