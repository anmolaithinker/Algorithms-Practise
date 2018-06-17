def Compare(a , b):
	l1 = a[1][0]
	t1 = a[1][1]
	l2 = b[1][0]
	t2 = b[1][1]
	return (l1 * t2) > (l2 * t1)


def GetJobSequencewithMinLoss(job):
	job_list = []
	for i in range(len(job)):
		job_list.append((i,job[i]))
	print 'New Jobs List : ' + str(job_list)	
	sort_ratio_list = sorted(job_list , cmp = Compare)
	print 'Sorted List : ' + str(sort_ratio_list)
	print '-----------------------------------------'
	print '-----------------------------------------'
	print 'Job Sequencing : '
	for i in sort_ratio_list:
		print str(i[0]) + ' -> '

	print '-----------------------------------------'
	print '-----------------------------------------'	


# (Loss for delay , Time Required By each job)
job = [(1,2),(2,4),(3,1),(5,3),(6,2)]
GetJobSequencewithMinLoss(job)


