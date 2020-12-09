"""
authors : Aartik(17075001)
		  Aditya Mittal(17075004)
		  Ankit Choudhary(17075011)

input   : take log.csv as input

output  : return the one hot encoded list of the events
		  and also return the remaining time of each event
"""

import csv

# mydatetime is python file which return diffrence between
# two timestamp in seconds.
import mydatetime

# read the data of log.csv and stores it in csvlog which
# is list of lists where each list contain all the feature
# of the event 
csvlog=open("../../Dataset/log.csv","r").read().split("\n")

event_number=0

for line in csvlog:
	line=line.split(",")
	csvlog[event_number]=line
	event_number+=1

noofrow=len(csvlog)-1                              #number of row in the dataset
noofcol=len(csvlog[0])                             #number of coloumn in dataset

maxtime=0.0

# return the one hot encoded list of the events
def encodedlist():
	newcol=[]										#consist of all the types of each feature							
	mapofcol=[]										#dictionary whaich conatin index of each feature
	temps=0


	for j in range(3,noofcol):
		temps=len(newcol)
		newcol.append([])
		for i in range(1,noofrow):
			if csvlog[i][j]=="":
				continue
			if(csvlog[i][j] not in newcol[j-3]):
				newcol[j-3].append(csvlog[i][j])
	k=0
	for i in range(len(newcol)):
		mapofcol.append({})
		for j in newcol[i]:
			mapofcol[i][j]=k
			k+=1
	encodedlist=[]
	for i in range(1,noofrow):
		for j in range(i,noofrow+1):
			if csvlog[i][0]!=csvlog[j][0]:
				j=j-1
				break

		# considering only those traces which ends with "Send for Credit Collection"
		if csvlog[j][3]!="Send for Credit Collection":
			continue
		rowlist=[]
		for j in newcol:
			for k in j:
				rowlist.append(0)
		for j in range(3,noofcol):
			for ii in range(i,0,-1):
				if(csvlog[ii][0]!=csvlog[i][0]):
					break
				if csvlog[ii][j]!="":
					rowlist[mapofcol[j-3][csvlog[ii][j]]]=1
					break

		# append encoded list of each event ot encodelist
		encodedlist.append(rowlist)

	return encodedlist



def makelabel():
	label=[]
	j=1
	final_time="-1"
	for i in range(1,noofrow):
		for j in range(i,noofrow+1):
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
	maxtime=1

	# maxtime stores the the maximum time among all the remaining time 
	for i in label:
		maxtime=max(i,maxtime)
	j=0

	# normalising the label data
	for i in label:
		label[j]=i/maxtime
		j+=1
	return label,maxtime