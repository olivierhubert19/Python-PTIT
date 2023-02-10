N = int(input())
l = []
dem=int()
for i in range(N):
    Check = input()
    if Check not in l:
        l.append(Check)
        dem+=1
print(dem)