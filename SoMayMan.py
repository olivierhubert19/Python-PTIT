from ctypes import sizeof
import string


a = input()
dem =int()
k=int(len(a))
for i in range(k):
    if a[i]=='4' or a[i]=='7':
        dem+=1
if dem==4 or dem==7 :
    print("YES")
else :
    print("NO")