import math

final_ans = []

def EgyptionFraction(fraction):
	num = fraction[0]
	den = fraction[1]

	print 'Numerator : ' + str(num)
	print 'Denominator : ' + str(den)

	if den <= 0 or num<=0:
		print '---------------------------------'
		print '---------------------------------'
		print 'Final Answer of this question : ' 
		for i in final_ans:
			print i
			print ' + '

		return 

	if den >= num:
		value = math.ceil(float(den/float(num)))
		print 'Ration of Den/Num : ' + str(value)

	ans = '1 / ' + str(value)	
	print 'Answer : ' + ans
	final_ans.append(ans)
	new_num = (num * value) - (den * 1)
	print 'New Numerator : ' + str(new_num)
	new_den = (den * value) 	
	print 'New Denominator : ' + str(new_den)
	print '-------------------------------------------'
	EgyptionFraction((new_num , new_den))


# Numerator , denominator
num = 6
den = 14
fraction = (num,den)

EgyptionFraction(fraction)