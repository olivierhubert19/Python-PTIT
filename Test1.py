import math

n = int(input())
coints = 0
cot = [0] *n
hang = [0]*n

for i in range (n):
    moi = input()
    for j in range(len(moi)):
        if moi[j] == 'C':
            cot[i] += 1
            hang[j] += 1

for i in cot:
    if i >= 2:
        coints += math.comb(i,2)
for i in hang:
    if i >= 2:
        coints += math.comb(i,2)

print(coints)