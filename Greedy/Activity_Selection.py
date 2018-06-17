

def SelectActivities(activity_time):

	# Sort the list according to finish time
	activity_time = sorted(activity_time , key = lambda x: x[1])

	# Checking Activity_time list
	print activity_time
	activity_list = []
	activity = activity_time[0]
	activity_list.append(activity)
	for i in activity_time:
		if (i[0] >= activity[1]):
			activity = i
			activity_list.append(activity)

	for i in activity_list:
		print 'Start Time : ' + str(i[0]) + ' ||  End Time : ' + str(i[1])
		print '----------------------------------' 		

# (start_time , end_time)
activity_time = [(5,9),(1,2),(3,4),(0,6),(5,7),(8,9)]

SelectActivities(activity_time)