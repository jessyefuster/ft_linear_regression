def parseDataset():
	dataset = { 'len': int, 'km': [], 'price': [] }

	try:
		with open('data.csv', 'r') as file:
			content = file.readlines()
			content = content[1:]

			for line in content:
				line = line[:-1]
				km, price = line.split(',')
				dataset['km'].append(float(km))
				dataset['price'].append(float(price))

			dataset['len'] = len(content)
			return (dataset)
	except:
		print("An error occured while reading file")


def storeValues(theta0, theta1):
	try:
		with open('values', 'w') as file:
			file.write("{},{}".format(theta0, theta1))
	except:
		print("An error occured while writing file")

def readValues():
	try:
		with open('values', 'r') as file:
			line = file.readline()
			theta0, theta1 = line.split(',')
			theta0, theta1 = float(theta0), float(theta1)

			return (theta0, theta1)
	except:
		print("An error occured while reading values file")
		return (0., 0.)

