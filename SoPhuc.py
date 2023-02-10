
class SoPhuc:
    def __init__(self,thuc,ao):
        self.thuc=thuc
        self.ao=ao
    
    def add(self,a):
        return  SoPhuc(self.thuc+a.thuc,self.ao+a.ao)
        
    def mull(self,a):
        return SoPhuc(self.thuc*a.thuc-self.ao*a.ao,self.ao*a.thuc+self.thuc*a.ao)
    
    def __str__(self):
        return str(int(self.thuc))+" + "+str(int(self.ao))+"i"

T = int(input())
for t in range(T):
    a,b,c,d = input().split()
    So1 = SoPhuc(int(a),int(b))
    So2 = SoPhuc(int(c),int(d))
    C=So1.add(So2)
    D=C.mull(C)
    C=C.mull(So1)
    print(str(C)+", "+str(D))