import math

class TramBom:
    def __init__(self,ten,luongMua, thoiGian, index):
        self.ma = "T{:02d}".format(index + 1)
        self.ten = ten
        self.luongMua = luongMua
        self.thoiGian = thoiGian
        self.tb = 0
        
    def boSung(self,thoiGian, luongMua):
        self.luongMua += luongMua
        self.thoiGian += thoiGian
        self.tb = round(self.luongMua / (self.thoiGian / 60) /1.0, 2)
    
    def __str__(self):
        return self.ma + ' ' + self.ten + ' ' + "{:.2f}".format(self.tb)
    
set ={""}
TD = []
n = int(input())
for i in range(n):
    #Công mồn lèo
    ten, batDau, ketThuc, luongMua = input(), input(), input(), int(input())
    
    gio1, gio2 = batDau.split(':'), ketThuc.split(':')
        
    thoiGian = (int(gio2[0]) - int(gio1[0])) * 60 + int(gio2[1]) + - int(gio1[1]) 
    
    if ten not in set:
        TD.append(TramBom(ten,luongMua,thoiGian,len(set) - 1))
    else:
        for j in TD:
            if j.ten == ten:
                j.boSung(thoiGian, luongMua)
    set.add(ten)
    
for i in TD:
    print(i)