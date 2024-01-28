# 程序文件 ex10_3_2.py
import numpy as np
import pylab as plt

x = np.arange(17, 30, 2)
a = np.loadtxt('data10_3.txt')
plt.rc('text', usetex=True)
plt.rc('font', size=16)
plt.plot(x, a[0], '*', label='$y_1$')
plt.plot(x, a[1], 'o', label='$y_2$')
x = np.hstack([x, x])
y = a.flatten()
p = np.polyfit(x, y, 2)
