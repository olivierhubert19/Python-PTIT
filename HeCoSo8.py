def sum(a):
    Sum=0
    if int(a[0])==1:
        Sum+=4
    if int(a[1])==1:
        Sum+=2
    if int(a[2])==1:
        Sum+=1
    return Sum
N = input()
if len(N)%3==1:
   N="00"+N
elif len(N)%3==2:
    N="0"+N
Res=""
for i in range(0,len(N)-2,3):
    Res=Res+str(sum(N[i:i+3]))
print(Res)