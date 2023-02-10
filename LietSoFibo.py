
a=[0,1]
for i in range(2,95,1):
    a.append(a[-1]+a[-2])
T = int(input())
while T>0:
    A,B = input().split()
    A=int(A)
    B=int(B)
    for i in range(A,B,1):
        print(a[i],end=' ')
    print(a[B])
    T-=1