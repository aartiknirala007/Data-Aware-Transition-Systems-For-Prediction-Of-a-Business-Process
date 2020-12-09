"""
Authors: Ankit Choudhary (17075011)
         Aditya Mittal (17075004)
         Aartik (17075001) 
"""

"""
In this file we are training our data
by using Support Vector Regressor
"""

import preprocessing
import numpy as np
from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV

# we use the one hot coded vectors as our feature set
feature=preprocessing.myencodedlist()

# for every event we set it's label to be the remaining time in its completion
# rangelabel  is  the maximum time recorded in our  dataset
label,rangelabel=preprocessing.makelabel()

length=len(feature)   

# we have used 5 cross validation 
# 20% data for test set and 80% for training set 
train_feature=feature[0:4*(length//5)]
train_label=label[0:4*(length//5)]

# we convert our training features and labels into a numpy array
X=np.array(train_feature)
Y=np.array(train_label)

# we set the range for parameters used in SVR
tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1,0.1],'C': [100,10,1,0.1], 'epsilon':[0.0001,0.00001]}]

# we use grid search for selecting the optimal combination of parameters to train our model
clf = GridSearchCV(SVR(), tuned_parameters,cv=5)

# we train our model using training data
clf.fit(X, Y) 

# print the best parameters for our model
print(clf.best_params_)

# we define a function that returns predicted and actual values of remaining time for any partial trace
def makeprediction():
	Predicted=[]
	Actual=[]

	# calculate the predicted values for the test set using the model trained by us
	Predicted=clf.predict(feature[4*(length//5):length])

	# actual values for the test set
	Actual=label[4*(length//5):length]
	return Predicted,Actual