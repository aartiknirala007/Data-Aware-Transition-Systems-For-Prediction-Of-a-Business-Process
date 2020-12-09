"""
In this file we convert a data from xes format to csv format 
and save it into log.csv.
"""



# create a dictionary trace and collect all data in it and
# a list key which stores all the features


XES_File = open("../Dataset/trafficdata.xes","r")

Trace_Count = 0
Event_Count = 0

trace = {}
keys = []

for line in XES_File:
	if(Trace_Count == 1300):
		break
	if(line == "</log>\n"):
		break
	if(line == "	<trace>\n"):
		Trace_Count+=1
		Event_Count=0
		continue
	if(line == "		</event>\n"):
		continue
	if(line == "	</trace>\n"):
		continue
	if(line == "		<event>\n"):
		Event_Count += 1
		trace[Trace_Number][Event_Count] = {}
		continue
	if(Trace_Count and not Event_Count):
		Trace_Description = list(line.split("\""))
		Trace_Number = Trace_Description[3]
		trace[Trace_Number] = {}
	if(Trace_Count and Event_Count):
		Event_Description = list(line.split("\""))
		key = Event_Description[1]
		value = Event_Description[3]
		if(key not in keys):
			keys.append(key)
		if(key not in trace[Trace_Number][Event_Count].keys()):
			trace[Trace_Number][Event_Count][key] = value


keys.append(keys[0])
keys.append(keys[1])
keys[0] = "Trace_Number"
keys[1] = "Case_Number"
for i in range(len(keys)):
	if(keys[i] == "time:timestamp"):
		keys[i] = keys[2]
		keys[2] = "time:timestamp"




# Writing in log.csv file



csvlist = []
logfile = open("../Dataset/log.csv","a+")
Event_Count = 0

for traces in trace.keys():
	Case_Number = 0
	for events in trace[traces].keys():
		csvlist.append([])
		csvlist[Event_Count].append(traces)
		csvlist[Event_Count].append(str(Case_Number))
		Feature_Number = 0
		for allkeys in keys:
			Feature_Number += 1
			if(Feature_Number == 1 or Feature_Number == 2):
				continue
			if(allkeys not in trace[traces][events].keys()):
				csvlist[Event_Count].append("")
				continue
			csvlist[Event_Count].append(trace[traces][events][allkeys])
		Case_Number += 1
		Event_Count += 1

length = len(keys)
Feature_Number = 0

for key in keys:
	logfile.write(key)
	if(Feature_Number != length-1):
		logfile.write(",")
	Feature_Number += 1

logfile.write("\n") 

for cases in csvlist:
	length = len(cases)
	Feature_Number = 0
	for value in cases:
		logfile.write(value)
		if(Feature_Number != length-1):
			logfile.write(",")
		Feature_Number += 1
	logfile.write("\n")