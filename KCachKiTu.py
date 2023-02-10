import math
def check(b):
    c=''
    for i in range(len(b)-1,-1,-1):
        c+=b[i]
    for i in range(len(b)-1):
        if  abs(ord(b[i])-ord(b[i+1]))!=abs(ord(c[i])-ord(c[i+1])):
            return 0
    return 1
a = int(input())
for i in range(a):
    b = input()
    if check(b) == 1:
        print("YES")
    else:
        print("NO")