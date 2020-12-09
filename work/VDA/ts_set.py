"""
authors : Aartik(17075001)
		  Aditya Mittal(17075004)
		  Ankit Choudhary(17075011)

input   : take log.csv as input

output  : return transiton system which contain information
		  regarding states, events, transitions, average time
		  of each transition and also returns the endstates
		  of the log.
"""


import csv

# mydatetime is python file which return diffrence between
# two timestamp in seconds.
import mydatetime

# read the data of log.csv and stores it in csvlog which
# is list of lists where each list contain all the feature
# of the event 
csvlog=open("../Dataset/log.csv","r").read().split("\n")
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

remtime=[]										   #remaining time of each events
avgremtime=[]									   #average of remaining time of each states

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

	# converting list to set and again into list
	curr_state=list(set(curr_state))

	# if the current state is new state then append it in states
	if curr_state not in states:
		total_states+=1
		states.append(curr_state)

	# if it is the last state of trace then append it into endstate
	if i==noofrow-1 or (csvlog[i][0]!=csvlog[i+1][0] and curr_state not in endstates) :
		endstates.append(curr_state)

for i in states:
	remtime.append([])

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
	curr_state=list(set(curr_state))
	for j in range(i,noofrow+1):
		if(csvlog[j][0]!=csvlog[i][0]):
			jj=j-1
			break

	# timediff is the remaining time of that states
	timediff=mydatetime.time_diff(csvlog[i][2],csvlog[jj][2])

	if csvlog[i][0]!=csvlog[i-1][0]:
		remtime[0].append(timediff)
	for ii in range(len(states)):
		if curr_state==states[ii]:
			remtime[ii].append(timediff)

# finding average time of each states
for i in range(len(remtime)):
	total_time=0
	for j in remtime[i]:
		total_time+=j

	# converting it into average time
	total_time=total_time/len(remtime[i])

	avgremtime.append(total_time)

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
	state_prev=list(set(state_prev))
	if csvlog[i][3] not in events:
		total_events+=1
		events.append(csvlog[i][3])
	state_after=state_prev.copy()
	event=csvlog[i][3]
	state_after.append(csvlog[i][3])
	state_after=list(set(state_after))

	# transition is a list which stores current transition
	transition=[state_prev,event,state_after]

	if transition not in transitions:
		total_transitions+=1
		transitions.append(transition)

# returns the Transition System
def TransitionSystem():
	return states,events,transitions,avgremtime

# returns the endstates
def endstate():
	return endstates
