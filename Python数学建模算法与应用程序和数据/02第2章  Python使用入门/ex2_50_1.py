# 程序文件 ex2_50_1.py
import sympy as sp
x1, x2 = sp.var('x1 x2')
s = sp.solve([x1**2+x2**2-1, x1-x2], [x1, x2])
print(s)
