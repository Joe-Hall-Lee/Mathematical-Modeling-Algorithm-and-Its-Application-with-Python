# 程序文件 ex7_8.py
import numpy as np
from scipy.interpolate import RegularGridInterpolator

z0 = np.loadtxt("data7_8.txt")  # 加载高程数据
x0 = np.linspace(100, 500, 5)
y0 = np.linspace(100, 400, 4)
points = (x0, y0)
f = RegularGridInterpolator(points, z0.T, 'cubic')  # 双三次样条插值
xn = np.linspace(100, 500, 41)
yn = np.linspace(100, 400, 31)
xxn, yyn = np.meshgrid(xn, yn)
zn = f((xxn, yyn))  # 计算插值点的函数值
zm = zn.max()  # 求矩阵元素的最大值
iy, ix = np.where(zn == zm)
print('x =', xn[ix])
print('y =', yn[iy])
print('最大高程为：', round(zm, 4))
