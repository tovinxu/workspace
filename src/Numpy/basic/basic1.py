# -*- coding: GBK -*-
'''
Created on 2013��9��8��

@author: tovin
'''
import numpy as np
from scipy.optimize.optimize import fmin_bfgs
a = np.arange(15).reshape(3,5)
print(a)
# ����n*m
print a.shape
#����ά��
print a.ndim
# Ԫ������
print a.dtype.name
# Ԫ�����ʹ�С
print a.itemsize
b = np.arange(1,120,2).reshape(3,4,5)
print b
c=np.linspace(1, 10, 20)
print c

# �������
a1=np.arange(1,10,2)
a2=np.arange(2,11,2)
print a1,a2
print a2-a1
print (a1**2)
print (a1*10)


#����˷�
print "����˷�"
b1=np.arange(1,8,2).reshape(2,2)
b2=np.arange(2,9,2).reshape(2,2)
print b1,b2
print b1*b2
# dot��������
print np.dot(b1,b2)


