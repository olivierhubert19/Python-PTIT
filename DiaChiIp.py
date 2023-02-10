T = int(input())
for t in range(T):
    IP=input()
    if len(IP)<7 :
        print("NO")
    else:
        try:
            IP=IP.split(".")
            if len(IP)!=4:
                print("NO")
            else:
                Check=True
                for i in IP:
                    if int(i)<0 or int(i)>255:
                        Check=False
                        break
                if Check:
                    print("YES")
                else:
                    print("NO")
        except:
            print("NO")    