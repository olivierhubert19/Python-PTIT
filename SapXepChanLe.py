n = int(input())
Check=n
A=[]
while True:
    data=[int(i) for i in input().split()]
    for i in data:
        A.append(i)
    Check-=len(data)
    if Check==0:
        break
Chan=[]
Le=[]
for i in A:
    if i%2==0:
        Chan.append(i)
    else:
        Le.append(i)
Chan.sort()
Le.sort(reverse=True)
C=0
L=0
for i in range(1,n+1):
    if A[i-1]%2==0 and C<len(Chan):
        print(Chan[C],end=" ")
        C+=1
    else:
        print(Le[L],end=" ")
        L+=1