#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 22:48:20 2018

@author: adarsh
"""

import numpy as np
import os,sys
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("Agg")
import pandas as pd
import cgitb; cgitb.enable()
import shutil
import pylab
os.environ[ 'HOME' ] = '/tmp/'

dataset=pd.read_csv("forestfires.csv")
dataset=dataset.drop(["month","day"],axis=1)
X=dataset.iloc[:,0:10].values
y=dataset.iloc[:,10].values

#plotting the region
plt.scatter(X[:,0:1],y,c='r')
pylab.savefig( "tempfile.png", format='png' )
shutil.copyfileobj(open("tempfile.png",'rb'), sys.stdout)
sb=plt.subplot(100,100,1)
pylab.savefig( "tempfile.png", format='png' )
shutil.copyfileobj(open("tempfile.png",'rb'), sys.stdout)
km=sb.plot(X,y,c='b',alpha=1)
pylab.savefig( "tempfile.png", format='png' )
shutil.copyfileobj(open("tempfile.png",'rb'), sys.stdout)


# split into test and train
from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)
print(len(x_train), len(y_train))

from sklearn.ensemble import RandomForestRegressor
random_forest = RandomForestRegressor()
random_forest.fit(x_train, y_train)
y_pred = random_forest.predict(x_test)

from sklearn.metrics import mean_squared_error
mse= mean_squared_error(y_test,y_pred)

for i in range(0,len(y_pred)):
    if(y_pred[i]>3):
        plt.scatter(x_test[i,0:1],y_pred[i],c='r')
    else:
        plt.scatter(x_test[i,0:1],y_pred[i],c='b')
plt.show()
