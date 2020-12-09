import train
import math
F,A=train.makeprediction()
n=0
k=0		
k1=0
a3=0
print(len(A),len(F))
for i in range(4*(len(A)//5),len(A)):
	a3+=A[i]
	if A[i]==0:
		continue
	k+=abs(A[i]-F[i])/A[i]
	k1+=(abs(A[i]-F[i])/A[i])*(abs(A[i]-F[i])/A[i])
	n+=1
# print(2,a3)
# pq.sort()
# print(pq)
print(n)
MAPE=k/n
RMSEP=math.sqrt(k1/n)
print(100*MAPE,100*RMSEP)