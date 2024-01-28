# 程序文件 ex10_4_2.py
import numpy as np
import pylab as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression as LR

a = np.loadtxt('data10_4.txt')
x1 = a[0]
x2 = a[1]
y = a[2]
plt.rc('text', usetex=True)
plt.rc('font', size=16)
plt.plot(x1, y, '*', label='$x_1$')
plt.plot(x2, y, 'o', label='$x_2$')
p = PolynomialFeatures(2)
xx = p.fit_transform(a[:2].T)
md = LR().fit(xx, y)
yh = md.predict(p.fit_transform([[160, 170]]))
