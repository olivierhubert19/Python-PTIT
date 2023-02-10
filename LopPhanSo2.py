from math import gcd

class PhanSo:
    def __init__(self,tu,mau):
        self.tu=tu
        self.mau=mau
    
    def giam(self):
        uoc = int(gcd(self.tu,self.mau))
        self.tu/=uoc
        self.mau/=uoc
    
    def add(self,a):
        self.tu=int(self.tu*a.mau+self.mau*a.tu)
        self.mau=int(self.mau*a.mau)
                
    def __str__(self):
        return str(int(self.tu))+"/"+str(int(self.mau))

Check=4
N=[]
while Check>0:
    data=input()
    for i in data.split():
        N.append(i)
        Check-=len(data.split())
       
a = PhanSo(int(N[0]),int(N[1]))
a.giam()
b = PhanSo(int(N[2]),int(N[3]))
b.giam()
a.add(b)
a.giam()
print(a)