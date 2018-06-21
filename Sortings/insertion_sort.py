
# Insertion sorting
# Time Complexity = O(n^2)
# Space Complexity = O(1)
def InsertionSort(arr):
	for i in range(0,len(arr)):
		key = arr[i]
		j = i-1
		while j>=0 and arr[j]>key:
			arr[j + 1] = arr[j]
			j = j-1
		arr[j+1] = key

	# Display	
	for i in arr:
		print i		

arr = [2,3,1,3,4,5,2,6,4]
InsertionSort(arr)	
