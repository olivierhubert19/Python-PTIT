Test = int(input())
for i in range(Test):
    N=input()
    check=''
    Check1=int()
    Ans=int()
    for i in range(len(N)):
        if ord(N[i])>=48 and ord(N[i])<=57:
            Check1=Check1*10+int(N[i])
        else:
            if Ans == 0 and Check1!=0 :
                Ans=Check1
            if Ans !=0 and Check1 !=0: 
                if Ans<Check1:
                    Ans=Check1
            Check1=int()
    if Ans !=0 and Check1 !=0: 
                if Ans<Check1:
                    Ans=Check1
    print(Ans)
            