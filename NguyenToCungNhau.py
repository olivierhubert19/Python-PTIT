from math import gcd

K =int(input())
N = list(set([int(i) for i in input().split()]))
N.sort()
K=len(N)
for i in range(K-1):
    for j in range(i+1,K):
        if gcd(N[i],N[j])==1:
            print(str(N[i])+" "+str(N[j]))   