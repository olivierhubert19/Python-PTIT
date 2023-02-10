a = int(input())
for i in range(a):
    b=input()
    tich=1
    for i in range(len(b)):
        if b[i]!='0':
            tich*=int(b[i])
    print(tich)