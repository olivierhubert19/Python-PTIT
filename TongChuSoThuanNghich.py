
from xml.etree.ElementTree import tostring, tostringlist


T = int(input())
for i in range(T):
    N=input()
    Tong=int()
    for j in range(len(N)):
        Tong+=int(N[j])
    Check=str(Tong)
    Check1=Check[::-1]
    if Check1==Check and len(Check)>1:
        print("YES")
    else:
        print("NO")
    