a = int(input())
for i in range(a):
    n = int(input())
    if n % 2 == 0 :
        dem = float()
        for i in range(2,n+1,2):
            dem += float(1/i)
        print("{:.6f}".format(dem))
    else :
        dem = float()
        for i in range(1,n+1,2):
            dem += float(1/i)
        print("{:.6f}".format(dem))
        