
# Partition
# [2,3,1,3,4,5,6,9]

def Partition(arr , p, r):
	# last pivot point
	x = arr[r]
	i = p-1
	for j in range(p,r):
		if arr[j] <= x:
			i = i+1
			arr[i] , arr[j] = arr[j] , arr[i]
	arr[i+1] , arr[r] = arr[r] , arr[i+1]
	return i+1

def QuickSort(arr , p , r):
	if p<r:
		q = Partition(arr , p , r)
		QuickSort(arr , p , q-1)
		QuickSort(arr , q+1 , r)


def printArray(array):
	for i in array:
		print i

array = [2,1,3,4,1,5,6,7,3]
print 'Before Sorting ----------------------->>>>>>'
printArray(array)
print '---------------------------------------------'
QuickSort(array,0,len(array)-1)
print '---------------------------------After Sorting -----------?>>>>'
printArray(array)		
print '------------Ohh Yeah!!------------------------------------------'





