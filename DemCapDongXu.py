N = int(input())
A=[]
dem=0
for i in range(N):
    A.append(input())
    
for i in range(N):
    Check=0
    for j in range(N):
        if A[i][j]=='C':
            Check+=1
    dem+=Check*(Check-1)/2
    Check=0
    for j in range(N):
        if A[j][i]=='C':
            Check+=1
    dem+=Check*(Check-1)/2
    
print(int(dem))
    