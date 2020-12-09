import ts_set
import csv
import mydatetime

A=[]
P=[]
csvlog=open("../Dataset/log.csv","r").read().split("\n")
j=0
for i in csvlog:
	i=i.split(",")
	csvlog[j]=i
	j+=1
noofrow=len(csvlog)-1
k=noofrow
noofcol=len(csvlog[0])
a4=0
states,events,transitions,avgremtime=ts_set.TransitionSystem()
for i in range(1,noofrow//5):
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
	curr_state=list(set(curr_state))
	for j in range(i,noofrow+1):
		if(csvlog[j][0]!=csvlog[i][0]):
			jj=j-1
			break
	timediff=mydatetime.time_diff(csvlog[i][2],csvlog[jj][2])
	A.append(timediff)
	if not curr_state in states:
		print(curr_state) 
	for i in range(len(states)):
		if states[i]==curr_state:
			# print(i,len(avgremtime),len(states))
			a4+=avgremtime[i]
			P.append(avgremtime[i])
# print(4,a4)
def makeprediction():
	return P,A
