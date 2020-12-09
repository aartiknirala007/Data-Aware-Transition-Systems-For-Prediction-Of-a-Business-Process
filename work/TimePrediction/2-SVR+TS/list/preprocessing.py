"""
authors : Aartik(17075001)
		  Aditya Mittal(17075004)
		  Ankit Choudhary(17075011)

input   : take log.csv as input

output  : return the one hot encoded list of the events
		  and also return the remaining time of each event
"""


import ts_list
import csv

# mydatetime is python file which return diffrence between
# two timestamp in seconds.
import mydatetime

states,events,transitions=ts_list.TransitionSystem()

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

encodedlist=[]

trace_start=1
states.append(['start'])

for i in range(1,noofrow):
	for j in range(i,noofrow+1):

		# finding the end event of that trace
		if csvlog[i][0]!=csvlog[j][0]:
			j=j-1
			break

	# considering only those traces which ends with "Send for Credit Collection"
	if csvlog[j][3]!="Send for Credit Collection":
		continue

	curr_list=[]
	for ii in range(len(states)):
		curr_list.append(0)

	# initialising every state with "start"
	curr_state=['start']

	if csvlog[i][0]!=csvlog[i-1][0]:
		trace_start=i
	for ii in range(trace_start,i+1):
		curr_state.append(csvlog[ii][3])
	temp=0
	for ii in states:
		if ii==curr_state:
			break
		temp+=1
	if temp!=len(states):
		curr_list[temp]=1
	else:
		curr_list=similarity(curr_state)

	# append encoded list of each event ot encodelist
	encodedlist.append(curr_list)



label=[]
j=1
final_time="-1"
for i in range(1,noofrow):
	for j in range(i,noofrow+1):

		# finding last event of hte trace
		if csvlog[i][0]!=csvlog[j][0]:
			j=j-1
			break

	# considering only those traces which ends with "Send for Credit Collection"
	if csvlog[j][3]!="Send for Credit Collection":
		continue

	# finding last event of hte trace
	for j in range(i,noofrow):
		if(j==noofrow-1 or csvlog[j+1][0]!=csvlog[i][0]):
			break

	# taking time diffrence between the two timestamp
	timediff=mydatetime.time_diff(csvlog[i][2],csvlog[j][2])
	label.append(timediff)
	j+=1

# maxtime stores the the maximum time among all the remaining time
maxtime=1
for i in label:
	maxtime=max(i,maxtime)

j=0
for i in label:
	label[j]=i/maxtime
	j+=1


# return the one hot encoded list of the states
def myencodedlist():
	return encodedlist

# normalising the label data
def makelabel():
	return label,maxtime

		
