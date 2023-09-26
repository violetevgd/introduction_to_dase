a = list(map(int, input().split()))
n = len(a)
b = [1 for _ in range(0, n)]
for i in range(0, n):
    for j in range(0, n):
        if(i == j):
            continue
        b[i] *= a[j]
print(b)