import math
import sys
from array import array
 
 
tong = 0
n = 2*10**6
res = array('i',[0]*(n+1))
for i in range(2,int(math.sqrt(n))+1):
	if res[i] == 0:
		res[i] = i
		for j in range(n//i + 1): res[i*j] = i
for i in range(4,n+1): res[i] += res[i//res[i]] if res[i] else i

n = int(input())
while True:
    try:
        N = int(sys.stdin.readline())
        tong+=res[N]
    except:
        break
print(int(tong))