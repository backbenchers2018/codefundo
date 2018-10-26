import cgitb
cgitb.enable()    
print("Content-Type: text/html;image/jpg\r\n\r\n")

import sys
import os

import numpy as np

import matplotlib

matplotlib.use('Agg')


import pandas as pd
from scipy.misc import imread
dataset=pd.read_csv("forestfires.csv")
dataset=dataset.drop(["month","day"],axis=1)
X=dataset.iloc[:,0:10].values
y=dataset.iloc[:,10].values
area=dataset.iloc[:,1].values
#plotting the region
img=imread('sample.jpg')


from io import StringIO,BytesIO
import matplotlib.pyplot as plt
import base64
html1 = """<img src="/sample.jpg" alt="FUCK" width="300" height="200"/> """
		
		
#print(html1)



# split into test and train

x_train=X[:413,2:10]
y_train=y[:413]
x_test=X[413:,2:10]
y_test=y[413:]
#print(len(x_train), len(y_train))

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)


# Applying PCA
from sklearn.decomposition import PCA
pca = PCA(n_components = 1)
x_train = pca.fit_transform(x_train)
x_test = pca.transform(x_test)
explained_variance = pca.explained_variance_ratio_



from sklearn.ensemble import RandomForestRegressor
random_forest = RandomForestRegressor()
random_forest.fit(x_train, y_train)
y_pred = random_forest.predict(x_test)

x11=x_test[:]
z1=y_pred[:]



from sklearn.metrics import mean_squared_error
mse= mean_squared_error(y_test,y_pred)




def doit():
    
    #
    for i in range(0,len(z1)):
    	if z1[i]>5:
    		if z1[i]>3 and z1[i]<=6:
    			plt.scatter(x11[i],z1[i],color='red',s=10**2)
    	else:
    		if z1[i]>3 and x11[i]>1:
    			plt.scatter(x11[i],z1[i],color='blue')
    plt.xticks(np.arange(0,10,step=1.0))
    plt.yticks(np.arange(0,11, step=1.0))
    plt.gca().invert_yaxis()
    
    
    plt.imshow(img, zorder=0, extent=[0.5, 10.0, 1.0, 7.0])
    
    format = "png"
    sio = BytesIO() 
    
    plt.savefig(sio, format='png')
    sio.seek(0)

    html = """<html>
    <head>
    </head>
    <body>
         <center><h1>Graphical Representation of Predictions</h1><center></br> 
         <p>Red-Dot--&gt Burnt Area Prediction Exceeds 5KMsq</p> 
        <p>Blue-Dot--&gt Burnt Area Prediction Less than 5KMsq</p>
		<img src="data:image/png;base64,{}"/>
        </body></html>""".format(base64.encodebytes(sio.getvalue()).decode()) 
    print(html)

doit()

#print(y_pred)



   
