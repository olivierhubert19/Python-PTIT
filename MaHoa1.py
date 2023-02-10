from xml.etree.ElementTree import tostring


a = int(input())
for i in range(a):
    b=input()
    dem = 1
    check = b[0]
    for i in range(1,len(b)):
        if b[i]!=check:
            if dem != 0 :
                print("%d%s"%(dem,check),end="")
                check = b[i]
                dem=1
        else:
            dem+=1
    print("%d%s"%(dem,check))
            