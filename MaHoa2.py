from ast import Try
P = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
while True:
    try:
        A,B=input().split(maxsplit=1)
        A=int(A)
        for i in range(len(B)-1,-1,-1):
            j = int()
            while(P[j]!=B[i]): j+=1
            print(P[(j+A)%28],end='')
        print()
    except:
        break