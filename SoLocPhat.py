test = int(input())
for i in range(test):
    s = str(input())
    sl = len(s)
    if sl >=2 and s[sl-2] == '8' and s[sl-1] =='6':
        print('YES')
    else:
        print('NO')