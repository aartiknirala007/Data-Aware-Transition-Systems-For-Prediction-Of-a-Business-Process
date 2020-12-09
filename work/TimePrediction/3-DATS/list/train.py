"""
Authors: Ankit Choudhary (17075011)
         Aditya Mittal (17075004)
         Aartik (17075001) 
"""

"""
In this file we are training our data
by using Support Vector Regressor
"""

import numpy as np 
import annotatedts
import ts_set
from sklearn.model_selection import GridSearchCV

states,events,transitions=ts_set.TransitionSystem()

# we use the one hot coded vectors as our feature set
state_len,NB,feature_data,label_data=annotatedts.ts()
from sklearn.svm import SVR
Actual=[]# we set the range for parameters used in SVR
Predicted=[]
clf=[]
count=0
for i in range(len(transitions)):
	l=len(feature_data[i])
	if(l<=6):
		continue
	# we have used 5 cross validation 
	# 20% data for test set and 80% for training set 
	test_feature=feature_data[i][0:4*(l//5)]
	test_label=label_data[i][0:4*(l//5)]

	# we convert our training features and labels into a numpy array
	X=np.array(test_feature)
	Y=np.array(test_label)

	# we set the range for parameters used in SVR
	tuned_parameters = [{'kernel': ['rbf'], 'gamma': [0.01,0.001],'C': [1,0.1,0.01,0.001], 'epsilon':[0.01,0.001]}]

	# we use grid search for selecting the optimal combination of parameters to train our model
	clfi = GridSearchCV(SVR(), tuned_parameters,cv=5)

	# we train our model using training data
	clfi.fit(X, Y) 

	# print the best parameters for our model
	print(clfi.best_params_)

	clf.append(clfi)
	Pi=[]
	Ai=[]

	# calculate the predicted values for the test set using the model trained by us
	Pi=clf[count].predict(feature_data[i][4*(l//5):l])

	# actual values for the test set
	Ai=label_data[i][4*(l//5):l]

	count+=1
	Actual.append(Ai)
	Predicted.append(Pi)
def makeprediction():
	return Predicted,Actual