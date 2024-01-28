# 程序文件 ex2_5_1.py
import os

fn = [filename for filename in
      os.listdir('D:\Python\WPy64-31140b1')
      if filename.endswith(('.exe', '.py'))]
print(fn)
