from math import sqrt
def Prime(n):
    if n<2:
        return False
    if n==2 or n==3:
        return True
    if n%2==0:
        return False
    for i in range(2,int(sqrt(n))+2):
        if n%i==0:
            return False
    return True

def sum(x):
    sum = 0
    for i in x:
        sum += int(i)
    return sum

def chr(x):
    for i in x:
        if i not in ['2','3','5','7']: return False
    return True

T = int(input())
for t in range(T):
    inp = input()
    n = int(inp)
    if (Prime(n) and Prime(int(inp[::-1])) and Prime(sum(inp)) and chr(inp)):
        print('Yes')
    else: print('No')