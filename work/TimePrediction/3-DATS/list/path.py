"""
authors : Aartik(17075001)
		  Aditya Mittal(17075004)
		  Ankit Choudhary(17075011)

input   : take log.csv as input

output  : return transiton system which contain information
		  regarding states, events, transitions of each 
		  transition and also returns the endstates of the log.
"""


import csv
import ts_set
import shortestp
import annotatedts
states,events,transitions=ts_set.TransitionSystem()
state_len,NB,feature_data,label_data=annotatedts.ts()
end=ts_set.endstate()
csvlog=open("../../../Dataset/log.csv","r").read().split("\n")
j=0
# print(csvlog)
for i in csvlog:
	i=i.split(",")
	csvlog[j]=i
	j+=1
noofrow=len(csvlog)-1
noofcol=len(csvlog[0])
tot=0
corr=0
for i in range(1,noofrow):
	for j in range(i,noofrow+1):
		if csvlog[i][0]!=csvlog[j][0]:
			j=j-1
			break
	if csvlog[j][3]!="Send for Credit Collection":
		continue
	curr_state=['start']
	if csvlog[i][0]!=csvlog[i-1][0]:
		trace_start=i
	for ii in range(trace_start,i+1):
		curr_state.append(csvlog[ii][3])
	if(i==36):
		print(curr_state)
		mypath=shortestp.findpath(curr_state,end,states,NB)
		print(mypath)
