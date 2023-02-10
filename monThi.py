class monThi:
    def __init__(self,maMonTHi,tenMonThi,hinhThucThi) :
        self.maMonThi = maMonTHi
        self.tenMonThi = tenMonThi
        self.hinhThucThi = hinhThucThi
    def getmaMonThi(self):
        return self.maMonThi

def soSanh(a):
    b = a.getmaMonThi
    return str(b)


N = int(input())
DS=[]
for i in range(N):
    maMonThi = input().strip()
    tenMonThi = input().strip()
    hinhThucThi = input().strip()
    monthi = monThi(maMonThi,tenMonThi,hinhThucThi)
    DS.append(monthi)
DS.sort(key=soSanh)
for i in DS:
    print(i.maMonThi+" "+i.tenMonThi+" "+i.hinhThucThi)