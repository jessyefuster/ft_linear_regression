# import graphics

def	hypothesis(inputValue, theta0 = 0.0, theta1 = 0.0):
	"""
	This is a linear function
	"""
	result = theta0 + (theta1 * inputValue)
	return (result)


def sumCosts0(dataset, theta0, theta1):
	costSum = 0.0

	for entry in dataset:
		costSum += hypothesis(entry[0], theta0, theta1) - entry[1]
	
	return (costSum)


def sumCosts1(dataset, theta0, theta1):
	costSum = 0.0

	for entry in dataset:
		costSum += ( hypothesis(entry[0], theta0, theta1) - entry[1] ) * entry[0]
		
	return (costSum)


def trainingAlgorithm(dataset, theta0, theta1):
	"""
	Here we are trying to guess the optimal value of theta0 and theta1
	according to the dataset
	The training algorithm is a Gradient Descent
	"""
	learningRate = 0.0001
	dataLen = float(len(dataset))

	while True:
		gradient0 = learningRate * ( sumCosts0(dataset, theta0, theta1) / dataLen )
		gradient1 = learningRate * ( sumCosts1(dataset, theta0, theta1) / dataLen )

		theta0 -= gradient0
		theta1 -= gradient1

		if abs(gradient0) < 0.001 and abs(gradient1) < 0.001:
			return (theta0, theta1)

	return (theta0, theta1)


if __name__ == '__main__':

	dataset = (
		(240000.0, 3640.0),
		(139800.0, 3800.0),
		(150500.0, 4400.0),
		(185530.0, 4450.0),
		(260000.0, 3450.0)
	)

	theta0, theta1 = trainingAlgorithm(dataset, 0.0, 0.0)
	print("Theta0 : {}\nTheta1 : {}".format(theta0, theta1))

	# print("The output value is {}".format(outputValue))
