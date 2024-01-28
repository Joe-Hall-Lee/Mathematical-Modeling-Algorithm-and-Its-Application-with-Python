# 程序文件 ex2_15.py
import math  # 导入标准库 math
import random  # 导入标准库 random

import numpy.random as nr  # 导入 numpy 库中的 random 模块

a = math.gcd(12, 21)  # 计算最大公约数，a = 3
b = random.randint(0, 2)  # 获得 [0, 2] 区间上的随机整数
c = nr.randint(0, 2, (4, 3))  # 获得 [0, 2) 区间上的 4 × 3 随机整数矩阵
print(a);
print(b);
print(c)  # 输出a, b, c的值
