# 程序文件 ex2_40.py
import numpy as np
import pandas as pd

d = pd.DataFrame(np.random.randint(1, 6, (10, 4)), columns=list("ABCD"))
d1 = d[:4]  # 获取前 4 行数据
d2 = d[4:]  # 获取第 5 行以后的数据
dd = pd.concat([d1, d2])  # 数据行合并
s1 = d.groupby('A').mean()  # 数据分组求均值
s2 = d.groupby('A').apply(sum)  # 数据分组求和
