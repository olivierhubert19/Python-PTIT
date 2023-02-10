import sys
T = int(input())
for i in range(1,T+1):
    s1=[i for i in sys.stdin.readline()]
    s2=[i for i in sys.stdin.readline()]
    s1.sort()
    s2.sort()
    if s1==s2:
        Ans="YES"
    else:
        Ans="NO"
    print("Test %d: "%i+Ans)