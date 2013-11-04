# -*- coding: GBK -*-
'''
Created on 2013年11月4日

@author: tovin
'''

import scipy as sp
import numpy as np
import matplotlib.pyplot as pt
from cProfile import label
from scipy.optimize.minpack import leastsq

def redise(p0,x,y):
    a,b = p0
    return (y-(a*x**2+b))

data = sp.genfromtxt("web_traffic.tsv", "\t");

y = data[:,1]
x = data[:,0]

x_clean = x[np.where(y>-1)]
y_clean = y[np.where(y>-1)]

rs = leastsq(redise, [0,0], args=(x_clean,y_clean));
print rs,rs[0]
y_predit = rs[0][0]*x_clean**2 + rs[0][1]

pt.plot(x_clean,y_clean,'.');
pt.plot(x_clean,y_predit,'-')
pt.show()