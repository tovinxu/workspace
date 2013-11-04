# -*- coding: GBK -*-
'''
Created on 2013年9月8日

@author: tovin
'''
import numpy as np
from scipy.optimize.optimize import fmin_bfgs
a = np.arange(15).reshape(3,5)
print(a)
# 数组n*m
print a.shape
#数组维数
print a.ndim
# 元素类型
print a.dtype.name
# 元素类型大小
print a.itemsize
b = np.arange(1,120,2).reshape(3,4,5)
print b
c=np.linspace(1, 10, 20)
print c

# 数组操作
a1=np.arange(1,10,2)
a2=np.arange(2,11,2)
print a1,a2
print a2-a1
print (a1**2)
print (a1*10)


#数组乘法
print "数组乘法"
b1=np.arange(1,8,2).reshape(2,2)
b2=np.arange(2,9,2).reshape(2,2)
print b1,b2
print b1*b2
# dot求矩阵相乘
print np.dot(b1,b2)


