# 程序文件 ex2_38_1.py
import numpy as np
import pandas as pd

dates = pd.date_range(start='20191101', end='20191124', freq='D')
a1 = pd.DataFrame(np.random.randn(24, 4), index=dates, columns=list('ABCD'))
a2 = pd.DataFrame(np.random.randn(24, 4))
a1.to_excel('data2_38_1.xlsx')
a2.to_csv('data2_38_2.csv')
f = pd.ExcelWriter('data2_38_3.xlsx')  # 创建文件对象
a1.to_excel(f, "Sheet1")  # 把 a1 写入 Excel 文件
a2.to_excel(f, "Sheet2")  # 把 a2 写入另一个表单中
f.close()
