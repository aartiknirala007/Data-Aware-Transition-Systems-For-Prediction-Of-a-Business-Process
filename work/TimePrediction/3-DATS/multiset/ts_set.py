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

# mydatetime is python file which return diffrence between
# two timestamp in seconds.
import mydatetime

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
endstates=[]                                       #list which stores all the states where trace ends
states=[]                                          #all the states in the dataset
events=[]										   #all the events in dataset
transitions=[]									   #all the transition from one state to another								 
statedic={}										   #dictiobary of all the states
eventsdic={}									   #ditionary of all the events
transitionsdic={}								   #dictionary of the transition
total_states=0									   #total number of states
total_events=0									   #total number of event
total_transitions=0                                #total number of transition

trace_start=1                                      #starting positon of the current trace
states.append(['start'])							


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


	for ii in range(trace_start,i+1):
		curr_state.append(csvlog[ii][3])

	curr_state=sorted(curr_state)

	# if the current state is new state then append it in states
	if curr_state not in states:
		total_states+=1
		states.append(curr_state)

	# if it is the last state of trace then append it into endstate
	if i==noofrow-1 or (csvlog[i][0]!=csvlog[i+1][0] and curr_state not in endstates) :
		endstates.append(curr_state)

state_prev=[]
state_after=[]
for i in range(1,noofrow):
	for j in range(i,noofrow+1):
		if csvlog[i][0]!=csvlog[j][0]:
			j=j-1
			break

	# considering only those traces which ends with "Send for Credit Collection"
	if csvlog[j][3]!="Send for Credit Collection":
		continue

	state_prev=['start']
	if csvlog[i][0]!=csvlog[i-1][0]:
		trace_start=i
	for ii in range(trace_start,i):
		state_prev.append(csvlog[ii][3])
	if csvlog[i][3] not in events:
		total_events+=1
		events.append(csvlog[i][3])
	state_after=state_prev.copy()
	event=csvlog[i][3]
	state_after.append(csvlog[i][3])

	state_after=sorted(state_after)
	state_prev=sorted(state_prev)

	# transition is a list which stores current transition
	transition=[state_prev,event,state_after]

	if transition not in transitions:
		total_transitions+=1
		transitions.append(transition)

# returns the Transition System
def TransitionSystem():
	return states,events,transitions

# returns the endstates
def endstate():
	return endstates
