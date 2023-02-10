a = int(input())
for i in range(a):
    b = int(input())
    print("1 * ",end='')
    k = 2
    while(k*k <= b):
        if b % k == 0:
            dem = 0
            while b % k == 0:
                dem += 1
                b/=k
            if b>1:
                print(str(k)+"^"+str(dem)+" * ",end='')
            else:
                print(str(k)+"^"+str(dem),end='')    
        else :
            k+=1             
    if b>1 :
        b=int(b)
        print(str(b)+"^1")
    else: 
        print()