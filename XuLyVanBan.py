import re

str = input()
str = re.split('[.?!]', str)
for i in str:
    if len(i) > 0:
        x = re.sub('\s+',' ',i.strip())
        print(x[0].upper()+x[1:].lower())
        print(type(x))
        print(x[0])
        