import itertools
A=[1,2,3,4]
B=[4,3,2,1]
print(A==B)

S = input()
S = [i for i in S]
S = itertools.permutations(S,len(S))
for s in S:
    for i in s:
        print(i,end="")
    print()