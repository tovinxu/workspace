
# -*- coding: GBK -*-
'''
Created on 2013年11月2日

@author: asus
'''

from scipy.optimize.optimize import fmin_bfgs
from numpy.ma.core import zeros

def rosen(x,p1,p2):   
        return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)  

    
x0 = [1.3, 0.7, 0.8, 1.9, 1.2]  
xopt = fmin_bfgs(rosen, x0,args=[1,1]) 