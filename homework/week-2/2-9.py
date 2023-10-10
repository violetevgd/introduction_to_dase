import math
import random
def Fx(num):
    return num * num + 4 * num * math.sin(num)

n = 0
m = 10000000
for i in range(m):
    x = random.uniform(2,3)
    y = random.uniform(0,100)
    if(y < Fx(x)):
        n += 1
ans = n / m * 100
print(ans)
