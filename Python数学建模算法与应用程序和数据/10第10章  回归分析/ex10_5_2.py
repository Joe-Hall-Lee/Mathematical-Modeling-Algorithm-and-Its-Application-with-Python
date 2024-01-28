# 程序文件 ex10_5_2.py
import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.preprocessing import PolynomialFeatures as PF
from sklearn.linear_model import LinearRegression as LR

a = pd.read_excel('data10_5.xlsx', header=None)
b = a.values
Y = np.hstack([b[:, 1], b[:-1, 6]])
X = np.vstack([b[:, 2:5], b[:-1, 7:]])
XX = np.hstack([np.ones((25, 1)), X])
md1 = sm.OLS(Y, XX).fit()
print(md1.summary())
XX2 = XX.copy()
XX2 = np.delete(XX2, 1, axis=1)
md2 = sm.OLS(Y, XX2).fit()
print(md2.summary())
p = PF(2)
xp = p.fit_transform(X)
md = LR().fit(xp, Y)  # 拟合完全二次式模型
print(md.coef_)  # 输出变量系数，二次项系数按照字典排序法排列
print(md.intercept_)  # 输出常数项
