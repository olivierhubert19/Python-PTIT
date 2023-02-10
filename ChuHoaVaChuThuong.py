s = str(input())
b=int(len(s))
dem1=int()
dem2=int()
for i in range(0,b) :
    if s[i].islower() == True : 
        dem1+=1
    else : 
        dem2+=1

if dem1 < dem2 : 
    print(s.upper())
else : 
    print(s.lower())
