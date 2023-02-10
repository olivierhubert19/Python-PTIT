# how to sorted class?
class NV:
    def __init__(self,id,name,diem):
        self.id=id
        self.name=name
        self.diem=diem
    
    def TrangThai(self):
        if self.diem >= 9.5:
            return "XUAT SAC"
        elif self.diem >= 8:
            return "DAT"
        elif self.diem >= 5:
            return "CAN NHAC"
        else:
            return "TRUOT"
    
    def __str__(self):
        return self.id+" "+self.name+" "+"%.2f"%self.diem+" "+self.TrangThai()

def diem(a):
    return a.diem
DS=[]
N = int(input()) 
for i in range(N):
    id = "TS0"+str(i+1)
    name=input().strip()
    d1=float(input())
    if d1>10:
        d1/=10
    d2=float(input())
    if d2>10:
        d2/=10
    tb = round((d1+d2)/2,2)
    DS.append(NV(id,name,tb))
DS.sort(key=diem,reverse=True)

for i in DS:
    print(i)
           