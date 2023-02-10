Check = 10
N = []
while Check>0:
    data = input()
    for i in data.split():
        N.append(int(i))
    Check-=len(data.split())
Ans=set()
for i in N:
    Ans.add(i%42)
print(len(Ans))
