num1 = int(input("请输入第一个数字："))
num2 = int(input("请输入第二个数字："))
m = max(num1, num2)
n = min(num1, num2)
r = m % n
while r != 0:
    m = n
    n = r
    r = m % n
    print(n)
