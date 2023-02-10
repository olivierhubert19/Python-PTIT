from math import sqrt
def UCLN(A,B):
    if B == 0 :
        return A
    else :
        return UCLN(B,A%B)

a = int(input())
for i in range(a):
    C,D = input().split()
    K = UCLN(int(D),int(C))
    M = int()
    while(K!=0):
        M+=int(K%10)
        K/=10
    K = int(M)
    flag = True
    if (K < 2):
        flag = False
    elif (K == 2):
        flag = True
    elif (K % 2 == 0):
        flag = False
    else:
        for i in range(3, K, 2):
            if (K % i == 0):
                flag = False
    if flag == True:
        print("YES")
    else:
        print("NO")