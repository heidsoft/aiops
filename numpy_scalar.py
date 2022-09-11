#!.venv/bin/python
# 标量： 仅包含一个数字的张量叫做标量， 0阶张量或0D张量

import numpy as np # 导入numpy 

X = np.array(5) #创建0D张量，也就是标量

print("X的值",X)
print("X的阶",X.ndim) #ndim 属性显示标量的阶
print("X的数据类型",X.dtype) #dtype属性显示标量的数据类型
print("X的形状",X.shape) #shape 属性显示标量的形状
