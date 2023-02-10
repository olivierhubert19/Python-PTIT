import gc
from math import gcd
from re import A


a = int(input())
a = input().split()
a = [int(i) for i in a]
a = sorted(a)
for i in range(0,len(a)-1):
    for j in range(i+1,len(a)):
        if gcd(a[i],a[j]) ==1:
            print(a[i],end=" ")
            print(a[j])