import math

def minimum_product(arr):

	product = 1
	count_neg = 0
	count_pos = 0
	count_zero = 0
	max_neg = -9999
	for i in range(len(arr)):
		if arr[i] < 0:
			count_neg = count_neg + 1
			max_neg = max(max_neg , arr[i])
			product = product * arr[i]
		elif arr[i] > 0:
			count_pos = count_pos + 1	
			product = product * arr[i]

		elif arr[i] == 0:
			count_zero = count_zero + 1	
	
	print 'Max_Neg : ' + str(max_neg)	
	if count_zero == len(arr):
		return 0	
	elif (not (count_neg and 1)):
		return 	((product/(max_neg)))
	elif ((count_neg and 1)):
		return product	


arr = [ -2 , -1 , -2 , 2 , 3]
print minimum_product(arr)		

arr = [ -1 , -2 , -3 , -2 , 2 , 1]
print minimum_product(arr)

arr = [-1 , 0]
print minimum_product(arr)

arr = [0 ,0 ,0 ,0]
print minimum_product(arr)

# [ -2 , -1 , -2 , 2 , 3]
# ans - -24

# [ -1 , -2 , -3 , -2 , 2 , 1]
#ans - -24

# [-1 , 0]
# ans - -1

# [0 ,0 ,0 ,0]
# ans - 0