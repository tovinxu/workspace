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
from numpy.lib.polynomial import polyfit

def redise(p0,x,y):
    a,b = p0
    return (y-(a*x+b))

data = sp.genfromtxt("web_traffic.tsv", "\t");

y = data[:,1]
x = data[:,0]

x_clean = x[np.where(y>-1)]
y_clean = y[np.where(y>-1)]

rs1 = leastsq(redise, [0,0], args=(x_clean,y_clean));
rs2 = polyfit(x_clean,y_clean,2,full=True)
rs5 = polyfit(x_clean,y_clean,25,full=True)  


y_predit1 = rs1[0][0]*x_clean + rs1[0][1]
y_predit2 = sp.poly1d(rs2[0]);
y_predit5 = sp.poly1d(rs5[0]);


pt.plot(x_clean,y_clean,'.');
pt.plot(x_clean,y_predit1,'-',label="predit1")
pt.plot(x_clean,y_predit2(x_clean),'-',label = "predit2")
pt.plot(x_clean,y_predit5(x_clean),'-',label = 'predit5')
pt.legend()
pt.show()