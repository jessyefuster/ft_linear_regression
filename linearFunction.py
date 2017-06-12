from parse import readValues

def	hypothesis(inputValue, theta0 = 0.0, theta1 = 0.0):
	"""
	This is the linear function
	"""
	result = theta0 + (theta1 * inputValue)
	return (result)

if __name__ == '__main__':
	
	try:
		mileage = input("\nPlease enter a mileage: ")
		mileage = float(mileage)

		theta0, theta1 = readValues()

		result = hypothesis(mileage, theta0, theta1)
		print("\nEstimated price: {}\n".format(result))
	except ValueError:
		print("Please enter a valid integer or float")

