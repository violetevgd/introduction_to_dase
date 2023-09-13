a = [1, 2, 3, 4, 5]
n = len(a)
#for
for x in range(n - 1):
    for y in range(x + 1, n):
        if(a[x] < a[y]):
            a[x], a[y] = a[y], a[x]
print(a)

#while
b = [1, 2, 3, 4, 5]
n = len(b)
c = 0
while(c in range(n - 1)):
    d = c + 1
    while(d in range(c + 1, n)):
        if(b[c] < b[d]):
            b[c], b[d] = b[d], b[c]
        d += 1
    c += 1
print(b)


