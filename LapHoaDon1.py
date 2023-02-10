class KH:
    def __init__(self,id,name,old,new):
        self.id=id
        self.name=name
        self.old=old
        self.new=new
    
    def used(self):
        return self.new-self.old
    
    def money(self):
        if self.used()>100:
            return round((((self.used()-100)*200)+12500)*1.05)
        elif self.used()>50:
            return round((((self.used()-50)*150)+5000)*1.03)
        return round(self.used()*100*1.02,0)
    
    def __str__(self):
        return str(self.id)+" "+str(self.name)+" "+str(int(self.money()))

DS=[]    
N = int(input())
for n in range(1,N+1):
    if n>=10:
        id="KH"+str(n)
    else:
        id="KH0"+str(n)
    name = input()
    old = int(input())
    new = int(input())
    DS.append(KH(id,name,old,new))

DS.sort(key=lambda x: -x.used())

for n in range(0,N):
    print(DS[n])    

    
    