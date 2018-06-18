
# Amazon interview

# Search an element in an array where difference between adjacent elements is 1


# Linear Search
def linearsearch(arr,key):
	for i in range(len(arr)):
		if arr[i] == key:
			return i

# Optimized Search
def optimizedSearch(arr,key):
	i = 0
	while i<len(arr):
		if arr[i] == key:
			return i
		i = i + abs(arr[i] - key)	



arr = [8 ,7, 6, 7, 6, 5, 4, 3, 2, 3, 4, 3]

# Linear Search
print 'Lineear Search : ' + str(linearsearch(arr , 3))

# Optimized Search
print 'Optimized Search : ' + str(optimizedSearch(arr,3))