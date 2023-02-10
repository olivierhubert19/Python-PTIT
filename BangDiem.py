class HS:
    def __init__(self,name,arr,id):
        self.name=name
        self.arr=arr
        self.id=id
    
    def tb(self):
        res=self.arr[0]*2+self.arr[1]*2
        for i in range(2,10):
            res+=self.arr[i]
        return round(res/12+0.01,1)
    
    def xeploai(self):
        if self.tb()>=9:
            return "XUAT SAC"
        elif self.tb()>=8:
            return "GIOI"
        elif self.tb()>=7:
            return "KHA"
        elif self.tb()>=5:
            return "TB"
        else:
            return"YEU"
    
    def __str__(self):
        return self.id+" "+self.name+" "+str(self.tb())+" "+self.xeploai()
    
DS=[]
for ds in range(1,int(input())+1):
    if ds<10: id="HS0"+str(ds)
    else: id="HS"+str(ds)
    name=input()
    arr=[float(i) for i in input().split()]
    DS.append(HS(name,arr,id))
DS.sort(key= lambda x : (-x.tb(),x.id))
for i in DS:
    print(i)