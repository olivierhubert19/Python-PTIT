N = int(input())
dem=int()
N = input().split()
N = [int(i) for i in N]
for i in range(len(N)-1):
    if N[i]!=N[i+1]:
        dem+=1
print(dem)