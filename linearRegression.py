# import plotly.plotly as py
# import plotly.graph_objs as go
import math
from featureScaling import scale

def	hypothesis(inputValue, theta0 = 0.0, theta1 = 0.0):
	"""
	This is a linear function
	"""
	result = theta0 + (theta1 * inputValue)
	return (result)


def sumCosts0(dataset, theta0, theta1):
	costSum = 0.

	for i in range(0, dataset['len']):
		# x = scale(dataset, 'km', dataset['km'][i])
		# y = scale(dataset, 'km', dataset['price'][i])
		x = dataset['km'][i]
		y = dataset['price'][i]
		costSum += hypothesis(x, theta0, theta1) - y

	return (costSum)


def sumCosts1(dataset, theta0, theta1):
	costSum = 0.

	for i in range(0, dataset['len']):
		# x = scale(dataset, 'km', dataset['km'][i])
		# y = scale(dataset, 'km', dataset['price'][i])
		x = dataset['km'][i]
		y = dataset['price'][i]
		costSum += ( hypothesis(x, theta0, theta1) - y ) * x

	return (costSum)

	# Bold Drive |  adapt learningRate at each iteration except first
	# if i:
	# 	if lastStep0 < sumFunction0:
	# 		learningRate0 /= 2.
	# 	else:
	# 		learningRate0 *= 1.1

	# 	if lastStep1 < sumFunction1:
	# 		learningRate1 /= 2.
	# 	else:
	# 		learningRate1 *= 1.1	

	# lastStep0, lastStep1 = sumFunction0, sumFunction1

def trainingAlgorithm(dataset, theta0, theta1):
	"""
	Here we are trying to guess the optimal value of theta0 and theta1
	according to the dataset
	The training algorithm is a Gradient Descent
	"""
	learningRate0, learningRate1 = 0.00001, 0.00001
	dataLen = float(len(dataset))

	while True:
		sumFunction0 = ( sumCosts0(dataset, theta0, theta1) / dataLen )
		sumFunction1 = ( sumCosts1(dataset, theta0, theta1) / dataLen )
		gradient0 = learningRate0 * sumFunction0
		gradient1 = learningRate1 * sumFunction1

		theta0 -= gradient0
		theta1 -= gradient1

		if not math.isnan(theta0) and not math.isnan(theta1):
			print(theta0, theta1)

		if abs(gradient0) < 0.00001 and abs(gradient1) < 0.00001:
			return (theta0, theta1)


if __name__ == '__main__':

	dataset = {
		'km':		[100., 200., 300., 400.],
		'price':	[300., 200., 300., 400.],
		'len':		4
	}

	# dataset = {
	# 	'km':		[1., 2., 3., 4.],
	# 	'price':	[3., 5., 7., 9.],
	# 	'len':		4
	# }

	# trace = go.Scatter(
	# 	x = [1, 2, 3, 4],
	# 	y = [1, 2, 3, 4],
	# 	mode = 'markers',
	# 	name = 'markers'
	# )

	# data = [trace]
	# py.iplot(data, filename='scatter-mode')

	theta0, theta1 = trainingAlgorithm(dataset, 0., 0.)

	print("Theta0 : {}\nTheta1 : {}".format(theta0, theta1))
	print("output for 250:")
	print(hypothesis(250., theta0, theta1))

	# print("The output value is {}".format(outputValue))
