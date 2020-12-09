import heapq
import math
parent=[0]
vis=[]
dist=[]
# print(parent)
def findpath(start,end,states,distance):
	parent=states.copy()
	st=0
	for i in states:
		if i==start:
			break
		st+=1
	vis=[0]*len(states)
	dis=[1000000000]*len(states)
	dis[st]=0
	li=[]
	heapq.heapify(li)
	heapq.heappush(li,(0,st))
	while(len(li)!=0):
		cur=heapq.heappop(li)[1]
		if not vis[cur]:
			vis[cur]=1
			for i in range(len(distance[cur])):
				if distance[cur][i]==0:
					continue
				if dis[i]>dis[cur]+abs((distance[cur][i])):
					dis[i]=dis[cur]+abs((distance[cur][i]))
					parent[i]=states[cur]
					heapq.heappush(li,(-dis[i],i))
	mini=1000000000
	for i in range(len(dis)):
		if(states[i] in end):
			mini=min(mini,dis[i])
	for i in range(len(dis)):
		if(states[i] in end and mini==dis[i]):
			pos=states[i]
			break
	return pos
				
# findpath(0,[0,1,2],[0,1,2],[[0,1,100],[1,0,5],[2,5,0]])
