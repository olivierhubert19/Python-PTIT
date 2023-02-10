from math import gcd
import string


test=int(input())
for i in range(test):
    b=input()
    c=''
    for i in range(len(b)-1,-1,-1):
        c+=b[i]  
    if gcd(int(b),int(c)) == 1:
        print("YES")
    else:
        print("NO")
        