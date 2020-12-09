"""
authors : Aartik(17075001)
		  Aditya Mittal(17075004)
		  Ankit Choudhary(17075011)

input   : transition system and a state

output  : return vector which is most similar to the
		 given state
"""

import ts_set

states,events,transitions=ts_set.TransitionSystem()
def similarity(given_state):
	# vector which have to be returned
	v=[]

	# sum of all the similarity values
	sumi=0

	# calculating similarity value
	for i in states:
		intersect=len((set(i)).intersection(set(given_state)))
		union=len((set(i)).union(set(given_state)))
		sumi+=intersect/union

	# normalising similarity values
	for i in states:
		intersect=len((set(i)).intersection(set(given_state)))
		union=len((set(i)).union(set(given_state)))
		pi=intersect/union
		v.append(pi/sumi)
	# print(v)
	return v