from math import gcd

class PhanSo:
    def __init__(self,tu,mau):
        self.tu=tu
        self.mau=mau
    def giam(self):
        uoc = gcd(self.tu,self.mau)
        self.tu/=uoc
        self.mau/=uoc
    def __str__(self):
        return str(int(self.tu))+"/"+str(int(self.mau))


if __name__=='__main__':
    tu,mau=input().split()
    a = PhanSo(int(tu),int(mau))
    a.giam()
    print(a)