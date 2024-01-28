# 程序文件 ex2_38_2.py
import numpy as np
import pandas as pd

dates = pd.date_range(start='20191101', end='20191124', freq='D')
a1 = pd.DataFrame(np.random.randn(24, 4), index=dates, columns=list('ABCD'))
a2 = pd.DataFrame(np.random.randn(24, 4))
a1.to_excel('data2_38_4.xlsx', index=False)  # 不包括行索引
a2.to_csv('data2_38_5.csv', index=False)  # 不包括行索引
f = pd.ExcelWriter('data2_38_6.xlsx')  # 创建文件对象
a1.to_excel(f, "Sheet1", index=False)  # 把 a1 写入 Excel 文件
a2.to_excel(f, "Sheet2", index=False)  # 把 a2 写入另一个表单中
f.close()
