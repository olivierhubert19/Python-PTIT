from xmlrpc.client import boolean


a = int(input())
for i in range(a):
    N = input()
    K=int()
    flag = True
    for j in range(len(N)):
        K+=int(N[i])
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