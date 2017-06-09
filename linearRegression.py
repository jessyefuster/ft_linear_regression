# import plotly.plotly as py
# import plotly.graph_objs as go
import math
import sys
from featureScaling import scale, getDecimalNumber

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


def trainingAlgorithm(dataset, theta0, theta1):
	"""
	Here we are trying to guess the optimal value of theta0 and theta1
	according to the dataset
	The training algorithm is a Gradient Descent
	"""
	learningRate0, learningRate1 = 10., 10.
	dataLen = float(dataset['len'])

	i = 0

	while True:
		sumFunction0 = ( sumCosts0(dataset, theta0, theta1) / dataLen )
		sumFunction1 = ( sumCosts1(dataset, theta0, theta1) / dataLen )
		gradient0 = learningRate0 * sumFunction0
		gradient1 = learningRate1 * sumFunction1

		if i:
			while abs(gradient0) > lastStep0:
				learningRate0 *= 0.8
				gradient0 = learningRate0 * sumFunction0

			while abs(gradient1) > lastStep1:
				learningRate1 *= 0.8
				gradient1 = learningRate1 * sumFunction1
		
		theta0 = theta0 - gradient0
		theta1 = theta1 - gradient1

		# print (theta0, theta1)

		# if i and abs(lastStep0 - abs(gradient0)) < 0.0000001 and abs(lastStep1 - abs(gradient1)) < 0.000001:
			# return (theta0, theta1)
		if math.isnan(theta0) and math.isnan(theta1):
			print("ERROR")
			sys.exit(1)

		if abs(gradient0) < 0.0000001 and abs(gradient1) < 0.0000001:
			return (theta0, theta1)
		
		lastStep0, lastStep1 = abs(gradient0), abs(gradient1)
		i = 1


if __name__ == '__main__':

	# dataset = {
	# 	'km':		[240000., 139800., 150500., 185530., 176000., 114800., 166800., 89000., 144500., 84000., 82029., 63060., 74000., 97500., 67000., 76025., 48235., 93000., 60949., 65674., 54000., 68500., 22899., 61789.],
	# 	'price':	[3650., 3800., 4400., 4450., 5250., 5350., 5800., 5990., 5999., 6200., 6390., 6390., 6600., 6800., 6800., 6900., 6900., 6990., 7490., 7555., 7990., 7990., 7990., 8290.],
	# 	'len':		24
	# }

	dataset = {
		'km':		[1., 2., 3., 4.],
		'price':	[3., 5., 7., 9.],
		'len':		4
	}

	# getDecimalNumber(0.00005)

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
	print("output for 2:")
	print(hypothesis(3., theta0, theta1))

	# print("The output value is {}".format(outputValue))
