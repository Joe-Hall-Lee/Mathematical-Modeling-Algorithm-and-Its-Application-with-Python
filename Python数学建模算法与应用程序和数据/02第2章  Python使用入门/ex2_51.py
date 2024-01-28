# 程序文件 ex2_51.py
import sympy as sp
a = sp.Matrix([[0, 0, 0, 1], [0, 0, 1, 0],
               [0, 1, 0, 0], [1, 0, 0, 0]])
print('特征值为：', a.eigenvals())
print('特征向量为：\n', a.eigenvects())
