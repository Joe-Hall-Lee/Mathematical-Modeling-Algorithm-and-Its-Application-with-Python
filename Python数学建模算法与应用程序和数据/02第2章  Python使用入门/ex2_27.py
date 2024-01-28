# 程序文件 ex2_27.py
import numpy as np

a = np.arange(16).reshape(4, 4)  # 生成 4 行 4 列的数组
b = a[1][2]  # 输出 6
c = a[1, 2]  # 同 b
d = a[1:2, 2:3]  # 输出 [[6]]
x = np.array([0, 1, 2, 1])
print(a[x == 1])  # 输出 a 的第 2、4 行元素
