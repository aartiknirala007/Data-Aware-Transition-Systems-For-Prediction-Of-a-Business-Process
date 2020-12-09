"""
authors : Aartik(17075001)
		  Aditya Mittal(17075004)
		  Ankit Choudhary(17075011)

input   : take two timestamp

output  : return the diffrence between the time in second
"""

from datetime import datetime
def time_diff(before,after):
	s1=after[0:19]
	s2=before[0:19]
	FMT = '%Y-%m-%dT%H:%M:%S'
	tdelta = datetime.strptime(s1, FMT) - datetime.strptime(s2, FMT)
	# converting the time into seconds
	ans=tdelta.days*24*60*60+tdelta.seconds
	return ans
