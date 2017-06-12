#!/usr/bin/python3
import math
import sys
import matplotlib.pyplot as plt

from parse import parseDataset, storeValues
from linearFunction import hypothesis

plt.ion()
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

def showGraph(t0, t1, clear=False):

	if clear:
		ax.clear()

	ax.plot(dataset['km'], dataset['price'], 'o', color='#008080')

	lineX = [0, 260000]
	lineY = [hypothesis(0, t0, t1), hypothesis(260000, t0, t1)]

	ax.plot(lineX, lineY, linestyle='dashed', color='#ff6600', linewidth=3.0)
	plt.pause(0.001)

def sumCosts0(dataset, theta0, theta1):
	costSum = 0.

	for i in range(0, dataset['len']):
		x = dataset['km'][i] * 0.001
		y = dataset['price'][i] * 0.001
		costSum += hypothesis(x, theta0, theta1) - y

	return (costSum)


def sumCosts1(dataset, theta0, theta1):
	costSum = 0.

	for i in range(0, dataset['len']):
		x = dataset['km'][i] * 0.001
		y = dataset['price'][i] * 0.001
		costSum += ( hypothesis(x, theta0, theta1) - y ) * x

	return (costSum)


def trainingAlgorithm(dataset, theta0, theta1, graph = False):
	"""
	Here we are trying to guess the optimal value of theta0 and theta1
	according to the dataset
	The training algorithm is a Gradient Descent
	"""
	learningRate0, learningRate1 = 0.0001, 0.0001
	dataLen = float(dataset['len'])

	i = 0

	while True:
		sumFunction0 = ( sumCosts0(dataset, theta0, theta1) / dataLen )
		sumFunction1 = ( sumCosts1(dataset, theta0, theta1) / dataLen )
		gradient0 = learningRate0 * sumFunction0
		gradient1 = learningRate1 * sumFunction1
		
		theta0 = theta0 - gradient0
		theta1 = theta1 - gradient1

		if math.isnan(theta0) and math.isnan(theta1):
			print("An error occured whith the selected parameters")
			sys.exit(1)

		if abs(gradient0) < 0.000001 and abs(gradient1) < 0.000001:
			return (theta0 * 1000., theta1)

		if graph:
			if i == 2000:
				i = 0
				showGraph(theta0 * 1000, theta1, True)
			else:
				i += 1



if __name__ == '__main__':
	graph = 'graph' in sys.argv

	dataset = parseDataset()
	theta0, theta1 = trainingAlgorithm(dataset, 0., 0., graph)
	storeValues(theta0, theta1)

	if graph:
		plt.ioff()
		plt.show()
