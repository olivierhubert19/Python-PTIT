import time
a = time.time()
limit=10**10
h = [1] * limit
x2, x3, x5 = 2, 3, 5
i = j = k = 0
for n in range(1, limit):
        h[n] = min(x2, x3, x5)
        if x2 == h[n]:
            i += 1
            x2 = 2 * h[i]
        if x3 == h[n]:
            j += 1
            x3 = 3 * h[j]
        if x5 == h[n]:
            k += 1
            x5 = 5 * h[k]
print(time.time()-a)