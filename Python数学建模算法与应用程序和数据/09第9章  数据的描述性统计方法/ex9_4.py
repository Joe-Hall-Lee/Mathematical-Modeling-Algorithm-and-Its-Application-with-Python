# 程序文件 ex9_4.py
from scipy.stats import expon
print(expon.stats(scale=3, moments='mvsk'))
