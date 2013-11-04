# -*- coding: GBK -*-
'''
Created on 2013年11月5日

@author: asus
'''

from sklearn.datasets.base import load_iris
from matplotlib import pyplot as plt
import numpy as np

data = load_iris();
print data['data']
print data['feature_names']
print data['target']
print data['target_names']

features = data['data']
feature_names = data['feature_names']
target = data['target']



for x in range(3):
    print x
    for t,marker,c in zip(xrange(3),">ox","rgb"):
# We plot each class on its own to get different colored markers
        plt.subplot(2,2,x+1)
     
        color = c,marker
        plt.scatter(features[target == t,x],features[target == t,x+1],c=c,marker=marker)
plt.show()