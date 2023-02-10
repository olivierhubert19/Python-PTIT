N = input()
A = set()
K = int()
if(len(N)%2==0): K=len(N)-3
else: K=len(N)-2
for i in range(0,K,2):
    A.add(int(N[i])*10+int(N[i+1]))
A = sorted(A)
for i in A :
    print(i,end=" ")