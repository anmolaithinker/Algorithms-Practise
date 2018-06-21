import math

# arr - array
# p - starting
# q - beech ka
# r - ending 
def merge(arr,p,q,r):
	left_array_size = q-p+1
	right_array_size = r-q
	l = []
	r = []
	for i in range(left_array_size):
		l.append(arr[p + i])

	for i in range(right_array_size):
		r.append(q + i + 1)	


# arr - array
# p - starting
# r - ending
def mergesort(arr,p,r):
	if p<r:
		q = math.floor(float(p + r) / 2)
		mergesort(arr,p,q)
		mergesort(arr,q+1,r)
		merge(arr,p,q,r)
