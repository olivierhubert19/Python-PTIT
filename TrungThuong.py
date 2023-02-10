T = int(input())
for t in range(T):
    n = int(input())
    count = {}
    for i in range(n):
        x = int(input())
        if x in count:
            count[x] = count[x] + 1
        else:
            count[x] = 1
    Max=0
    Key=0
    for key,val in count.items():
        if val>Max:
            Max=val
            Key=key
        elif val==Max and key<Key:
            Key=key   
    print(Key)