"""
Authors: Ankit Choudhary (17075011)
         Aditya Mittal (17075004)
         Aartik (17075001)
"""
"""
In this file we are calculating the result 
by finding their MAPE and RMSPE values
"""
# we import our model by importing  the train.py file
import train
import math
# we store the Predicted and actual values of remaining time in P, A respectively
Predicted,Actual=train.makeprediction()

NumberOfEvent=0
MAPE=0		
RMSEP=0
for i in range(len(Actual)):
	for j in range(len(Actual[i])):

		if Actual[i][j]==0:
			# if its the last event in the trace then we don't calculate the remaining time for it
			continue
		NumberOfEvent+=1
		#  we calculate the MAPE and RMSPE values 
		MAPE+=abs(Actual[i][j]-Predicted[i][j])/Actual[i][j]
		RMSEP+=(abs(Actual[i][j]-Predicted[i][j])/Actual[i][j])*(abs(Actual[i][j]-Predicted[i][j])/Actual[i][j])

MAPE=MAPE/NumberOfEvent
RMSEP=math.sqrt(RMSEP/NumberOfEvent)
print(100*MAPE,100*RMSEP)