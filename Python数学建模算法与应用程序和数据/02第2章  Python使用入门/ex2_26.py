# 程序文件 ex2_26.py
import numpy as np

a = np.ones(4, dtype=int)  # 输出 [1, 1, 1, 1]
b = np.ones((4,), dtype=int)  # 同 a
c = np.ones((4, 1))  # 输出 4 行 1 列的数组
d = np.zeros(4)  # 输出 [0, 0, 0, 0]
e = np.empty(3)  # 生成 3 个元素的空数组行向量
f = np.eye(3)  # 生成 3 阶单位阵
g = np.eye(3, k=1)  # 生成第 k 对角线的元素为 1，其他元素为 0 的 3 阶方阵
h = np.zeros_like(a)  # 生成与 a 同维数的全 0 数组
