test=int(input())
for i in range(test):
    N=input()
    if ord(N[0])==ord(N[len(N)-1]):
        print("YES")
    else:
        print("NO")