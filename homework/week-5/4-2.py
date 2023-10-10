import time

start_time = time.time()
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

a = int(input())
if is_prime(a):
    print("是质数")
else:
    print("不是质数")

end_time = time.time()

execution_time = end_time - start_time

print(f"程序执行时间为: {execution_time} 秒")
