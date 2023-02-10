class ThiSinh:
    def __init__(self,name,date,d1,d2,d3):
        self.name=name
        self.date=date
        self.d1=d1
        self.d2=d2
        self.d3=d3
        
    def __str__(self):
        tong=0
        tong+=(self.d1+self.d2+self.d3)
        return self.name+" "+self.date+" %.1f"%tong

name=input()
date=input()
d1=float(input())
d2=float(input())
d3=float(input())

a= ThiSinh(name,date,d1,d2,d3)
print(a)        