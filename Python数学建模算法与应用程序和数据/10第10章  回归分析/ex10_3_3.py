# 程序文件 ex10_3_3.py
import numpy as np
import pylab as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression as LR

x = np.arange(17, 30, 2)
a = np.loadtxt('data10_3.txt')
plt.rc('text', usetex=True)
plt.rc('font', size=16)
plt.plot(x, a[0], '*', label='$y_1$')
plt.plot(x, a[1], 'o', label='$y_2$')
x = np.hstack([x, x]).reshape(-1, 1)
y = a.flatten()
p = PolynomialFeatures(2)
xx = p.fit_transform(x)
md = LR().fit(xx, y)
print(md.coef_)  # 输出变量的系数
print(md.intercept_)  # 输出常数项
