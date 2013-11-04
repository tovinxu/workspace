# -*- coding: GBK -*-
'''
Created on 2013年9月9日

@author: asus
'''


import numpy as np
from matplotlib.pyplot import plot, legend

import matplotlib.pyplot as pl
from scipy.optimize.optimize import fmin_bfgs, fmin_cg
from scipy.optimize.minpack import leastsq
from cProfile import label
from scipy.optimize.lbfgsb import fmin_l_bfgs_b

def func1(p,*args):
    a,b=p
   
    x,y=args
    cost = np.sum((y- (a*x + b))**2);
    return  cost

def func(p,*args):
    a,b=p
   
    x,y=args
    cost = y- (a*x + b);
    return  cost

x = np.arange(1,10,1);
y_true = 3*x+ 4;
y_mean = y_true + 10*np.random.rand(len(x))

p0= np.array([1,2]);
print p0
rs1= fmin_bfgs(func1,[1,2],args=(x,y_mean))

rs2= fmin_cg(func1,[1,2],args=(x,y_mean))
rs = leastsq(func,p0,args=(x,y_mean));
# 
# rs1=fmin_bfgs(func,p0,args=(x,y_mean))

print "rs=",rs
# 
print "rs1=",rs1
print "rs2=",rs2
y1= rs[0][0]*x + rs[0][1]
y2 = rs1[0]*x + rs1[1]
pl.plot(x,y1,'r',label="y1");
pl.plot(x,y2,'b',label="y2");
pl.plot(x,y_mean,'og',label='y_mean');
pl.legend()
pl.show()