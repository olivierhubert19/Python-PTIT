def abs(n):
    if n<0:
        return -n
    return n


while True:
    N = [int(i) for i in input().split()]
    if N == [int(),int(),int(),int()]:
        break
    dem = 0
    while True:
        if N[0]==N[1] and N[1]==N[2] and N[2]==N[3]:
            break
        N0 = N[0]
        N[0] = abs(N[0]-N[1])
        N[1] = abs(N[1]-N[2])
        N[2] = abs(N[2]-N[3])
        N[3] = abs(N[3]-N0)
        dem+=1
    print(dem)