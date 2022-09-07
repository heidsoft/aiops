#!.venv/bin/python

import numpy as np
A = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
arr1 = np.array(A) # 将列表转为矩阵
print("A=",A)
print("通过列表A创建的矩阵arr1\n",arr1)

B=((1,2,3,4),(5,6,7,8),(9,10,11,12))
arr2 = np.array(B) # 将元组转为矩阵
print("B=",B)
print("通过列表A创建的矩阵arr2\n",arr2)

print("arr1的大小：",arr1.shape) #获取矩阵的规模