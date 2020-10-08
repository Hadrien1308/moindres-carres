#Méthode des moindres Carrés#

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

X=np.array([0,10,20,30,40,50,60,70,80,90])
Y=np.array([0,1,5,2.3,2.9,3.0,0,4.3,6.2,7.8])
plt.scatter(X,Y,color='r')

xm=np.mean(X)
ym=np.mean(Y)
num=0
den=0
for i in range(len(X)):
    num += (X[i]-xm)*(Y[i]-ym)
    den += (X[i]-xm)**2
a=num/den
b=ym-a*xm

print(a,b)

yp = a*X+b
plt.scatter(X,Y)
plt.plot(X,yp,'r')
plt.show()


