for t in range(int(input())):
    I,J,K=map(int,input().split())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    C = [int(i) for i in input().split()]
    A.sort()
    B.sort()
    C.sort()
    Check=False
    i,j,k=0,0,0
    while i<I and j<J and k<K:
        if A[i]==B[j]==C[k]:
            print(A[i],end=' ')
            Check=True
            i+=1
            j+=1
            k+=1
        elif A[i]==min(A[i],B[j],C[k]):
            i+=1
        elif B[j]==min(A[i],B[j],C[k]):
            j+=1
        elif C[k]==min(A[i],B[j],C[k]):
            k+=1
    if Check: print()
    else: print("NO")
                
            