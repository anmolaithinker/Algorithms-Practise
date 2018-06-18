
# Amazon Interview ( steps defined 2 or 3 )

# f(n) = f(n-2) + f(n-3)

def getCountsStairs(n):
	if (n==0):
		return 1
	if (n<0):
		return 0	
	two_steps = getCountsStairs(n-2)
	three_steps = getCountsStairs(n-3)
	return two_steps + three_steps	


storage = []

def storageFunc(n):
	# (n -> Result)
	for i in storage:
		if i[0] == n:
			return (True , i[1])

	return (False , False)		

def dpGetCountStairs(n):

	if n == 0:
		return 1
	if n<0:
		return 0
	a = storageFunc(n)	
	if a[0]:
		return a[1]		
	two_steps = getCountsStairs(n-2)
	three_steps = getCountsStairs(n-3)
	return two_steps + three_steps	


print 'Result : ' + str(dpGetCountStairs(10))

# for total stairs = 10
# 2 + 2 + 2 + 2 + 2
# 3 + 3 + 2 + 2
# 2 + 2 + 3 + 3
# 2 + 3 + 2 + 3
# 3 + 2 + 3 + 2	
# 3 + 2 + 2 + 3
# 2 + 3 + 3 + 2


# for total stairs = 5
# 2 + 3
# 3 + 2 