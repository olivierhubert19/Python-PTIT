A=[]
N = int(input())
for i in  range(N):
    A.append([int(i) for i in input().split()])
K = int(input())
low=0
high=0

for i in range(N):
    for j in range(N):
        if i+j+2>N+1:
            high+=A[i][j]
        elif i+j+2<N+1:
            low+=A[i][j]


if abs(low-high)>K:
    print("NO")
else:
    print("YES")
print(abs(low-high))