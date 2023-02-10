N = int(input())
N = [int(i) for i in input().split()]
Res=0
for i in range(len(N)-1):
    for j in range(i+1,len(N)):
        if N[i]>N[j]:
            Res+=1
print(Res)