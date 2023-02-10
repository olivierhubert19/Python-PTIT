N = int(input())
A=[int(i) for i in input().split()]
CheckMax=A[0]
CheckViTri=0
LenA=len(A)
Chia=0
if(LenA%2==0):
    Chia=LenA/2
else:
    Chia=int(LenA/2)
for i in range(1,LenA):
    if i<=(Chia):
        if CheckMax < i+1+A[i]:
            CheckMax=i+1+A[i]
            CheckViTri=i
        if CheckMax == i+1+A[i] and i>CheckViTri:
            CheckMax=i+1+A[i]
            CheckViTri=i
        
    else:
        if CheckMax < LenA-i+A[i]:
            CheckMax=LenA-i+A[i]
            CheckViTri=i
        if CheckMax == LenA-i+A[i] and LenA-i>CheckViTri:
            CheckMax=LenA-i+A[i]
            CheckViTri=i
            
Left=0
Right=LenA-1
MaxLeft=CheckViTri+A[0]-A[CheckViTri]
MaxRight=CheckViTri+A[LenA-1]-A[CheckViTri]

for i in range(1,CheckViTri):
    if MaxLeft< CheckViTri-i+1+A[i]-A[CheckViTri]:
        MaxLeft= CheckViTri-i+1+A[i]-A[CheckViTri]
        Left=i

for i in range(LenA-1,CheckViTri,-1):
    if MaxRight< CheckViTri-(LenA-i)+A[i]-A[CheckViTri]:
        MaxLeft= CheckViTri-(LenA-i)+A[i]-A[CheckViTri]
        Right=i
Ans=0
if (MaxLeft<MaxRight) :
    if A[CheckViTri]<=A[Right]:
        Ans+=A[Right]-A[CheckViTri]
        Ans+=CheckViTri-(LenA-Right)
        A[CheckViTri]+=Ans
        print(str(Ans)+"  1")
    else:
        if A[CheckViTri]-A[Right]+CheckViTri-(LenA-Right) <0:
            Ans+=A[CheckViTri]-A[Right]+CheckViTri-(LenA-Right)
            A[CheckViTri]+=Ans
            print(str(Ans)+"  2")
if(MaxRight>MaxLeft):
    if A[CheckViTri]<=A[Left]:
        Ans+=A[Right]-A[CheckViTri]
        Ans+=CheckViTri-Left
        A[CheckViTri]+=Ans
        print(str(Ans)+"  3")
    else:
        if A[CheckViTri]-A[Left]+CheckViTri-Left < 0:
            Ans+= abs(A[CheckViTri]-A[Left]+CheckViTri-Left)
            A[CheckViTri]+=Ans
            print(Left)
            print(str(Ans)+"  4")
if(MaxLeft==MaxRight and Left>LenA-Right):
    if A[CheckViTri]<=A[Left]:
        Ans+=A[Right]-A[CheckViTri]
        Ans+=CheckViTri-Left
        A[CheckViTri]+=Ans
        print(str(Ans)+"  5")
    else:
        if A[CheckViTri]-A[Left]+CheckViTri-Left < 0:
            Ans+= abs(A[CheckViTri]-A[Left]+CheckViTri-Left)
            A[CheckViTri]+=Ans
            print(Left)
            print(str(Ans)+"  6")
else:
    if A[CheckViTri]<=A[Right]:
        Ans+=A[Right]-A[CheckViTri]
        Ans+=CheckViTri-(LenA-Right)
        A[CheckViTri]+=Ans
        print(str(Ans)+"  7")
    else:
        if A[CheckViTri]-A[Right]+CheckViTri-(LenA-Right) <0:
            Ans+=A[CheckViTri]-A[Right]+CheckViTri-(LenA-Right)
            A[CheckViTri]+=Ans
            print(str(Ans)+"  8")

print(CheckViTri)            
print(A[CheckViTri])
for i in range(CheckViTri):
    Ans+=(A[CheckViTri]-A[i])-(CheckViTri-i)
    
print(Ans)
for i in range(LenA-1,CheckViTri,-1): 
    Ans+=A[CheckViTri]-A[i]+(CheckViTri-(LenA-i))
    
print(Ans)
 
  

        
            
