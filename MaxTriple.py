import re
from heapq import nlargest as MIN
for t in range(int(input())):
    n=input()
    n =input().replace(' ','  ')+' '
    sum=0
    count=0
    for i in range(8,-9,-1):
        if count>=3: break
        if i==0: continue
        str=' '
        if i<0: str='-'
        str+='\d'*abs(i)
        str+=' '
        check=MIN(3,[int(k) for k in re.findall(str,n)])
        while count<3 and len(check)>0:
            sum+=max(check)
            check.remove(max(check))
            count+=1
    print(sum)