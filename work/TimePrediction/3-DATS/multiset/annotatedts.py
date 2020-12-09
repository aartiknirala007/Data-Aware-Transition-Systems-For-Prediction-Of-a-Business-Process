"""
authors : Aartik(17075001)
		  Aditya Mittal(17075004)
		  Ankit Choudhary(17075011)

input   : Transition Systyem, log.csv

output  : return transiton system which contain information
		  regarding states, events, transitions, average time
		  of each transition and also returns the endstates
		  of the log.
"""

# ts_set is python file which return diffrence Transition
# system and end states of each trace
import ts_set

import csv

# onehotencoser is python file which onehotencode each event
# and return them alnog with their remaining time
import onehotencoder

# mydatetime is python file which return diffrence between
# two timestamp in seconds.
import mydatetime

# encodedlist is a list which stores encoded list of each event
encodedlist=onehotencoder.encodedlist()

states,events,transitions=ts_set.TransitionSystem()

# read the data of log.csv and stores it in csvlog which
# is list of lists where each list contain all the feature
# of the event 
csvlog=open("../../../Dataset/log.csv","r").read().split("\n")
event_number=0
for line in csvlog:
	line=line.split(",")
	csvlog[event_number]=line
	event_number+=1


noofrow=len(csvlog)-1                              #number of row in the dataset
noofcol=len(csvlog[0])                             #number of coloumn in dataset

feature_data=[]									   
label_data=[]
for i in transitions:
	feature_data.append([])
	label_data.append([])

trans_from_state=[]								   #it stores all the states which can be traverse from given state
for state in states:
	tss=[]
	for transition in transitions:
		if state==transition[0]:
			tss.append(transition[2])
	trans_from_state.append(tss)

state_len=[]									   #stores number of state which can be traverse from given state
for i in trans_from_state:
	state_len.append(len(i))

NB=[]											   #stores the probablity of transition from one state to another

for i in range(len(states)):
	NB.append([])
	for j in states:
		NB[i].append(0)

count=0

for i in range(1,noofrow):
	for j in range(i,noofrow+1):
		if csvlog[i][0]!=csvlog[j][0]:
			j=j-1
			break
	# considering only those traces which ends with "Send for Credit Collection"
	if csvlog[j][3]!="Send for Credit Collection":
		continue

	# initialising every state with "start"
	curr_state=['start']

	# assign the value to trace_start if the new trace begins
	if csvlog[i][0]!=csvlog[i-1][0]:
		trace_start=i

	for ii in range(trace_start,i):
		curr_state.append(csvlog[ii][3])
	next_state=curr_state.copy()
	next_state.append(csvlog[i][3])
	curr_state=sorted(curr_state)
	next_state=sorted(next_state)
	event=csvlog[i][3]
	transition=[curr_state,event,next_state]

	# seperate feature and label set on the basis of transition
	for ii in range(len(transitions)):
		if transitions[ii]==transition:
			feature_data[ii].append(encodedlist[count])
			for j in range(i,noofrow):
				if(csvlog[j][0]!=csvlog[i][0]):
					j=j-1
					break
			timediff=mydatetime.time_diff(csvlog[i][2],csvlog[j][2])
			label_data[ii].append(timediff)

	# NB[ii][iii] contains number of transition between ii and iii
	for ii in range(len(states)):
		if states[ii]==curr_state:
			for iii in range(len(states)):
				if states[iii]==next_state:
					NB[ii][iii]+=1
	count+=1

# converting the number into their possiblity
for i in range(len(NB)):
	sumi=0
	for j in range(len(NB[i])):
		sumi+=NB[i][j]
	if(sumi==0):
		continue
	for j in range(len(NB[i])):
		NB[i][j]/=sumi

# maximum time among all the remaining time
maxtime=1
for i in label_data:
	maxtime=max(max(i),maxtime)

# normalising the label_data 
for i in range(len(label_data)):
	for ii in range(len(label_data[i])):
		label_data[i][ii]/=maxtime

# returns the annotated Transition System
def ts():
	return state_len,NB,feature_data,label_data




