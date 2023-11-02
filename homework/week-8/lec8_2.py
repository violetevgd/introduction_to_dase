import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle
import numpy as np

x = [2, 4, 5, 3, 1, 2]
y = [1, 1, 3, 5, 3, 1]
plt.plot(x, y)
plt.rcParams['font.sans-serif']=['SimHei']
plt.title("五边形")#括号当中输入标题的名称
plt.show()

fig2 = plt.figure(num=2, figsize=(5, 5))
axes2 = fig2.add_subplot(1, 1, 1)
c = Circle(xy=(0.3, 0.3), radius=0.2, alpha=0.5, color='red')  # 圆
e = Ellipse(xy=(0.6, 0.6), width=0.2, height=0.4, alpha=0.8, angle=60, color='green')
axes2.add_patch(c)
axes2.add_patch(e)
plt.rcParams['font.sans-serif']=['SimHei']
plt.title("圆形和椭圆")
plt.show()

matplotlib.rcParams['axes.unicode_minus'] =False
x = np.linspace(0, 10, 1000)
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
plt.show()
