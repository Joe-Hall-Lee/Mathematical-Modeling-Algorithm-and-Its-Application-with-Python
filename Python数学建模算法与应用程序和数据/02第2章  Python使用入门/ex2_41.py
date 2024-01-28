# 程序文件 ex2_41.py
import numpy as np
import pandas as pd

a = pd.DataFrame(np.random.randint(1, 6, (5, 3)),
                 index=['a', 'b', 'c', 'd', 'e'],
                 columns=['one', 'two', 'three'])
a.loc['a', 'one'] = np.nan  # 修改第 1 行第 1 列的数据
b = a.iloc[1:3, 0:2].values  # 提取第 2、3 行，第 1、2 列数据
a['four'] = 'bar'  # 增加第 4 列数据
a2 = a.reindex(['a', 'b', 'c', 'd', 'e', 'f'])
a3 = a2.dropna()  # 删除有不确定值的行
