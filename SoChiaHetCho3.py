n = int(input())
for i in range(n):
    b = input()
    tong=int()
    for j in range(len(b)):
        tong+=int(b[j])
    if tong % 3 == 0 :
        print("YES")
    else: 
        print("NO")