# 程序文件 ex15_5.py
import numpy as np

with open('data15_5.txt') as f:
    s = f.read().replace('\n', '')
a = np.zeros((2, 2))  # 统计数据初始化
def mfind(s, c): return [x for x in range(s.find(c), len(s)) if s[x:x+2] == c]


for i in range(2):
    for j in range(2):
        a[i, j] = len(mfind(s, str(i)+str(j)))
print('统计数据矩阵 a:\n', a)
print('a 的行和:', a.sum(axis=1))
