Name = input().lower()
Len = len(Name)
Check=""
Check+=Name[Len-3]+Name[Len-2]+Name[Len-1]
if Check=='.py':
    print("yes")
else:
    print("no")