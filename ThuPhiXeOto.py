DS={}
for t in range(int(input())):
    Xe=input().split()
    if(Xe[3]=="IN"):
        if Xe[4] not in DS:
            DS[Xe[4]]=0
        if(Xe[1]=="Xe_con"):
            if(Xe[2]=="5"):
                DS[Xe[4]]+=10000
            else:
                DS[Xe[4]]+=15000
        if(Xe[1]=="Xe_tai"):
            DS[Xe[4]]+=20000
        if(Xe[1]=="Xe_khach"):
            if(Xe[2]=="29"):
                DS[Xe[4]]+=50000
            else:
                DS[Xe[4]]+=70000
for val,key in DS.items():
    print(str(val)+": "+str(key)) 