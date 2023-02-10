a = input()
dem = 0
for i in range(len(a)):
    dem+=1
    print(a[i],end='')
    if (len(a)-i-1) % 3 == 0 and i != len(a)-1:
        print(",",end='')