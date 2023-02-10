while True:
    N = int(input())
    if N == 0:
        break
    Ans = set()
    Ans.add(N)
    while(N!=1):
        if N%2==0:
            N/=2
        else:
            N=N*3+1
        Ans.add(N)
    print(len(Ans))
    