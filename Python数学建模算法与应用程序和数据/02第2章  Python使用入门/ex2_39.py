# 程序文件 ex_39.py
import pandas as pd

a = pd.read_csv("data2_38_2.csv", usecols=range(1, 5))
b = pd.read_excel("data2_38_3.xlsx", "Sheet2", usecols=range(1, 5))
c = pd.read_excel("data2_38_6.xlsx")  # 读第 1 个表单有表头数据
d = pd.read_excel("data2_38_6.xlsx", "Sheet2", header=None)  # 无表头
