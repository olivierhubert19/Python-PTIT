T=int(input())
for i in range(T):
    N=input()
    if len(N)%2==0 or int(N[0])==int(N[1]):
        print("NO")
    else:
        check=0
        for j in range(0,len(N)-3,2):
            if int(N[j]) != int(N[j+2]):
                print("NO")
                check=1
                break
        if check == 0:
            print("YES")