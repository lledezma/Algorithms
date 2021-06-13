import math
		#Scheduling competing activites 
def activity_selection(activities,k):
	n = len(activities)
	A = {}
	A[k] = activities[k]
	for m in range(1,n+1):
		if activities[m][0] >= activities[k][1]:
			A[m] = activities[m]
			k = m
	print(A)


activities = {1:[1,4], 2:[3,5], 3:[0,6], 4:[5,7], 5:[3,9], 6:[5,9], 7:[6,10], 8:[8,11], 
	9:[8,12], 10:[2,14], 11:[12,16]}

activity_selection(activities,4)