import numpy as pin
X=pin.array([[-1,-1],[-2,-1],[-3,-2],[1,1],[2,1],[3,2]])
Y=pin.array([-1,-1,-1,1,1,1])
from sklearn.naive_bayes import GaussianNB
val=GaussianNB()
val.fit(X,Y)
a=input()
b=input()
pred=val.predict([[a,b]])
print pred
