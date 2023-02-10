a = int(input())
for i in range(a):
    N=input()
    dem=int()
    check=N[0]
    for i in range(1,len(N)):
        if i % 2 == 1 :
            dem=int(N[i])
            for i in range(dem):
                print(check,end='')
        else:
            check=N[i]
    print()