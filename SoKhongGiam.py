n = int(input())
for i in range(n):
    a=input()
    check=int()
    for i in range(len(a)-1):
        if int(a[i])>int(a[i+1]):
            check=1
            break
    if check==1:
        print("NO")
    else:
        print("YES")