# 程序文件 ex7_14.py
import numpy as np
from scipy.optimize import curve_fit

a = np.loadtxt('data7_13.txt')
t0 = a[0]
y0 = a[1]
def y(t, k, m): return k*np.exp(m*t)


p, pcov = curve_fit(y, t0, y0)
print('拟合的参数为：', np.round(p, 4))
yh = y(np.array([5, 8]), *p)
print('预测值为：', np.round(yh, 4))
