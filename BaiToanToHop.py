import itertools
N,K = input().split()
K=int(K)
N=list(set(int(x) for x in input().split()))
N.sort()
res = itertools.combinations(N,K)
for i in res:
    print(*i)