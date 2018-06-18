


def allotment(arr , k):
	police = []
	theives = []
	for i in range(len(arr)):
		if arr[i] == 'P':
			police.append(i)
		elif arr[i] == 'T':
			theives.append(i)
	p = 0
	t = 0
	alloted = 0
	while(p<len(police) and t<len(theives)):
		if abs(police[p] - theives[t]) <= k:
			alloted = alloted + 1
			p = p+1
			t = t+1
		else:
			if police[p] < theives[t]:
				p = p+1
			else:
				t = t+1

	return alloted				
				


# Given array
arr = ['P' , 'T' , 'T' , 'P' , 'P']
k = 1
print 'Allotment  : ' + str(allotment(arr, k))