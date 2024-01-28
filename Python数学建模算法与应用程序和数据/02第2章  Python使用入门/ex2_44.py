# 程序文件 ex2_44.py
from scipy.optimize import fsolve, root


def fx(x): return x**980-5.01*x**979+7.398*x**978\
    - 3.388*x**977-x**3+5.01*x**2-7.398*x+3.388


x1 = fsolve(fx, 1.5, maxfev=4000)  # 函数调用 4000 次
x2 = root(fx, 1.5)
print(x1, '\n', '-------------')
print(x2)
