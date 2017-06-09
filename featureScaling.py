
def getNum0(string):
	zeros = 0
	for c in string:
		if c == '0':
			zeros += 1
		else:
			break
	return (zeros)

def getDecimalNumber(number):
	res = 0
	strNum = str(number)

	print(strNum.split('.'))

	# before, after = strNum.split('.')
	
	# if int(before) + int(after) == 0:
	# 	pass
	# elif int(before) > 0:
	# 	res = len(before) - 1
	# elif len(after) > 0:
	# 	res = (- (len(getNum0(after))))

	# print(number, res)


def scale(dataset, key, value):
	mean = sum(dataset[key]) / dataset['len']
	maxX = max(dataset[key])
	minX = min(dataset[key])

	return ( (value - mean) / (maxX - minX) )
