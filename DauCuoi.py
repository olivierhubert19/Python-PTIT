def dem(n):
    dem = int()
    while(n>0):
        n=int(n/10)
        dem+=1
    return dem
b = int(input())
for i in range(b) :
    b = int(input())
    k = dem(b)
    check = int()
    dem1 = int()
    dem2 = int()
    while(b>0):
        check+=1
        m = int(b % 10)
        if check == 1 :
            dem1+=m
        if check == 2 :
            dem1+=m*10
        if check == k-1 :
            dem2+=m
        if check == k :
            dem2+=m*10
        b=int(b/10)
    if dem1 == dem2 :
        print("YES")
    else: print("NO")