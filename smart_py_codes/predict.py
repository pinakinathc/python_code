# deploying Gaussian Naive Bayes algorithn to predict the values of unknown parameters
# based on a training set included in the code.

import numpy as pin
#the following is the feature training set
X=pin.array([[-1,-1],[-2,-1],[-3,-2],[1,1],[2,1],[3,2]])
#the following is the label training set
Y=pin.array([-1,-1,-1,1,1,1])
from sklearn.naive_bayes import GaussianNB
#classifying the classifier val as GaussianNB
val=GaussianNB()
#training the classifier by feeding it the training example
val.fit(X,Y)
a=input()
b=input()
#predicting values
pred=val.predict([[a,b]])
print pred
