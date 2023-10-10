import random
import math
import time

# 方法1：蒙特卡洛方法
def monte_carlo_pi(num_samples):
    inside_circle = 0
    for i in range(num_samples):
        x = random.random()
        y = random.random()
        distance = math.sqrt(x**2 + y**2)
        if distance <= 1:
            inside_circle += 1
    return (inside_circle / num_samples) * 4

# 方法2：零点计数法（Leibniz公式）
def leibniz_pi(num_terms):
    pi_estimate = 0
    for i in range(num_terms):
        term = (-1)**i / (2*i + 1)
        pi_estimate += term
    return pi_estimate * 4

# 方法3：高斯-勒让德积分法
def gauss_legendre_pi(num_iterations):
    a = 1.0
    b = 1.0 / math.sqrt(2)
    t = 0.25
    p = 1.0
    for i in range(num_iterations):
        a_next = (a + b) / 2
        b = math.sqrt(a * b)
        t -= p * (a - a_next)**2
        a = a_next
        p *= 2
    pi_estimate = (a + b)**2 / (4 * t)
    return pi_estimate

# 测试并比较效率
num_samples = 1000000
num_terms = 1000000
num_iterations = 10

start_time = time.time()
monte_carlo_result = monte_carlo_pi(num_samples)
monte_carlo_time = time.time() - start_time

start_time = time.time()
leibniz_result = leibniz_pi(num_terms)
leibniz_time = time.time() - start_time

start_time = time.time()
gauss_legendre_result = gauss_legendre_pi(num_iterations)
gauss_legendre_time = time.time() - start_time

print(f"蒙特卡洛方法计算π的值为：{monte_carlo_result}, 用时：{monte_carlo_time}秒")
print(f"零点计数法计算π的值为：{leibniz_result}, 用时：{leibniz_time}秒")
print(f"高斯-勒让德积分法计算π的值为：{gauss_legendre_result}, 用时：{gauss_legendre_time}秒")