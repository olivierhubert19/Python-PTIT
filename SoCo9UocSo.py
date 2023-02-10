N=[]
print(type(N))
Len=pow(10,9)
print(Len)
for i in range(Len+5):
    N.append(2)
Len1=int(Len/2)
print(Len1)
N[0]=0
N[1]=1
for i in range(2,Len1+1):
    N[i*i]+=1
    for j in range(i+1,Len1+1):
        N[i*j]+=2
for i in N:
    print(i)
    