from math import sqrt,pow

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def dis(self,a):
        return sqrt(pow((self.x-a.x),2)+pow((self.y-a.y),2))
    
    
if __name__=='__main__':
    Ans=[]
    T = int(input())
    for t in range(T):
        Check=6
        N=[]
        while Check>0:
            data=input()
            for i in data.split():
                N.append(float(i))
            Check-=len(data.split())
        Ans.append(N)
    for t in range(T):
        d1 = Point(Ans[t][0],Ans[t][1])
        d2 = Point(Ans[t][2],Ans[t][3])
        d3 = Point(Ans[t][4],Ans[t][5])
        if d1.dis(d2)+d1.dis(d3)<=d2.dis(d3) or d1.dis(d3)+d2.dis(d3)<=d1.dis(d2) or d2.dis(d3)+d1.dis(d2)<=d1.dis(d3):
            print("INVALID")
        else:
            P = d1.dis(d2)+d1.dis(d3)+d2.dis(d3)
            print("%.3f"%P)