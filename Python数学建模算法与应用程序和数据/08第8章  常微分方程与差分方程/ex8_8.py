# 程序文件 ex8_8.py
from scipy.integrate import odeint
import numpy as np
import pylab as plt


def yx(y, x): return [y[1], np.sqrt(1+y[1]**2)/5/(1-x)]


x0 = np.arange(0, 1, 0.00001)
y0 = odeint(yx, [0, 0], x0)
plt.rc('font', size=16)
plt.plot(x0, y0[:, 0])
plt.show()
