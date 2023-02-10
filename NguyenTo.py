def UCLN(A,B):
    if B == 0 :
        return A
    else :
        return UCLN(B,A%B)
    
def NguyenTo(n):
    if n < 2 :
        return 0
    if n == 2 : 
        return 1
    if n == 3 : 
        return 1
    if n % 2 == 0 :
        return 0
    for i in range(3,n-1,2):
        if n % i == 0 :
            return 0
    return 1

a = int(input())
for i in range(a):
    b = int(input())
    dem = int()
    for i in range(1,b,1):
        if UCLN(b,i) == 1 :
            dem+=1      
    if NguyenTo(dem) == 1:
        print("YES")
    else:
        print("NO")