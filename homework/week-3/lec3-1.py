num = eval(input())
num_int = int(num)
# 整数部分
s = []
while(num_int):
    s.append(num_int % 2)
    num_int = num_int // 2
s.reverse()

#小数部分
num_fra = num - int(num)
x = []
y = []
if(num_fra != 0):
    while(num_fra):
        num_fra = num_fra * 2
        x.append(int(num_fra))
        num_fra = num_fra - int(num_fra)
    for i in range(0, 10):
        y.append(x[i])
    print(f"{s},{y}")
else:
    print(f"{s}")