T = int(input())
for t in range(T):
    N = input()
    try:
        Check=True
        for i in N:
            if int(i)>2:
                Check=False
                break
        if Check:
            print("YES")
        else:
            print("NO")
    except:
        print("NO")